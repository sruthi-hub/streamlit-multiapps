import pybase64 as base64
import streamlit as st
import sys
import networkx as nx
import networkx.algorithms.approximation as nx_approx
import pandas as pd
import numpy as np
#from numexpr3 import evaluate as ev
from scipy.spatial.distance import cdist, pdist, squareform
import scipy.integrate as integrate
import time
import math  
import os
import csv

from numexpr import evaluate as ev
from tqdm import tqdm

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Sarcopenia Network Entropy Calculator")
st.markdown("This application is a streamlit Network Entropy Calculator that takes in two folders containing the edge list and node list separately and returns a spatial entropy value.") 

def giulia_config_spatial_entropy(edgelist,nodelist):
    
    start = time.time()
    
    #g = nx.read_edgelist(edgelist, delimiter=',')
    g = nx.from_pandas_edgelist(edgelist)
   
    edges=list(g.edges()) #added for debugging
    #st.write(edges)
    
    nodes = list(g.nodes())
    nodes.sort()

    PP = np.array(nx.to_numpy_matrix(g,nodelist=nodes))

    n = len(nodes)
    

    N=PP.shape[0];
    connectivity = np.sum(PP,1);
    avg_conn = np.mean(connectivity)
    #Lagrangians
    z = connectivity/(math.sqrt(avg_conn*N))
    old_z = z
    
    loops =5 #loops = 10000 #original loops value
    precision = 1

    for idx in tqdm(range(loops)):
        zT = z[:,np.newaxis]
        D = ev("(zT * z) + 1.")
        UD = ev("z/D")
        del D
        for i in range(N):  UD[i,i]=0.
        z = connectivity / np.sum(UD,1)
        rz= ev("abs(1.-z/old_z)")
        rz[np.isinf(rz)]=0.
        rz[np.isnan(rz)]=0.

        if max(rz)<precision:
            break
        old_z = z
    z2 = np.outer(z,z)
    for i in range(N):  z2[i,i]=0.
    P = z2 / ( z2 + 1)
    Q=1.-P
    CS = -1*(np.sum(np.log(P**P) + np.log(Q**Q) ))/2.
    # print "number of loops ", idx+1
    #stop = time.time()

    print("config entropy done once!!!")
    
    #start = time.time()
    
    #g = nx.read_edgelist(edgelist, delimiter=',')
#     nodes = list(g.nodes())
#     nodes.sort()

#     PP = np.array(nx.to_numpy_matrix(g,nodelist=nodes))

    n = len(nodes)
    print("I'm here...Number:", str(n))
    distance = np.zeros((n,n))

    #ens_id_expr_df = pd.read_csv(nodelist,names=['ens_id','expr_val'])
    ens_id_expr_df =nodelist
    ens_id_expr_df = ens_id_expr_df.set_index('ens_id')
    
    ens_id_expr_map = ens_id_expr_df.to_dict()['expr_val']
    #st.write(edgelist)

    for row in tqdm(range(n)): # first tqdm
        for col in range(n):
            #try:
            #st.write(nodes[row])
            #st.write(nodes[col])
            x = float(ens_id_expr_map[nodes[row]])
            y = float(ens_id_expr_map[nodes[col]])
#             st.write(x)
#             st.write(y)
            distance[row][col] = math.fabs(x-y)
            

            #except KeyError:
                #distance[row][col] = 0
                
                

    Nbin = int(math.sqrt(n)+1)
    
    print("Nbin:",Nbin)

    print("before linear binning...")
    #linear binning
    #st.write(distance)
    mi,ma = np.min(distance[distance>0]),np.max(distance)
    limiti = np.linspace(mi,ma,Nbin+1)
    limiti[-1]+=0.1*ma
    limiti[0]-=0.1*mi

    b = np.searchsorted(limiti,distance)-1

    print("before massimo...")
    massimo = np.max(b)+1
   
    # BC gives how many links fall in each bin
    BC = [ np.sum(b[PP>0]==i)/2 for i in range(massimo) ]
    
    print("BC:",BC)


    N=PP.shape[0];
    
    connectivity = np.sum(PP,1);
    avg_conn = np.mean(connectivity)

    print("before lagragian...")
    #Lagrangians
    z = connectivity/(math.sqrt(avg_conn*N))
    w = BC / (avg_conn*N)

    old_z = z
    old_w = w

    loops = 5  # CHANGE to 10000 again
        
    precision = 1E-5
    #precision = 1E-3 # CHANGED NOW!

    for idx in tqdm(range(loops)): # second tqdm
        bigW = w.take(b)

        for i in range(N):  bigW[i,i]=0.

        U = ev("bigW * z")
        UT = U.T    
        D = ev("(UT * z) + 1.")

        UD = ev("U/D")

        del D,U,UT
        


        for i in range(N):  UD[i,i]=0.

        z = connectivity / np.sum(UD,1)

        zt = z[:].reshape(N,1)
        D2 = ev("(z*zt) / ( bigW *(z*zt) + 1.)")

        B2 = np.array([np.sum(np.where(b==i,D2,0.)) for i in range(len(w))])/2.

        print("And calculating B2 AND D2 done!!!!! inside for loop out of 5")

        w = np.where( (BC!=0) & (B2!=0),BC/B2,0)
        rz= ev("abs(1.-z/old_z)")
        rw= ev("abs(1.-w/old_w)")
        rz[np.isinf(rz)]=0.
        rw[np.isinf(rw)]=0.
        rz[np.isnan(rz)]=0.
        rw[np.isnan(rw)]=0.

        if max(rz)<precision and max(rw)<precision:
            break

        old_z = z
        old_w = w
        
    print("JUST OUT OF THE BIG FORR LOOP...!")

    bigW = w.take(b)
    for i in range(N):  bigW[i,i]=0.

    z2 = bigW * np.outer(z,z)
    P = z2 / ( z2 + 1)
    Q=1.-P
    
    print("And calculations done!!!!!")
    S = -1*(np.sum(np.log(P**P) + np.log(Q**Q) ))/2.
#    S = -1*(np.sum((P*np.log(P)) + (Q*np.log(Q) )))/2.
    print("Done S  ....!!!!!")
    stop = time.time()

    output = dict()
    output['num_nodes'] = n
    output['num_edges'] = len(g.edges())
    output['giulia_config_entropy']=CS
    output['giulia_spatial_entropy'] = S
    output['entropy_subtracted_baseline']= S-CS
    output['runtime'] = stop-start
    output['nodelist'] = nodelist
    output['edgelist'] = edgelist

    return output
   
#creating a new csv file to write computed spatial entropy values and giving headers
fieldnames = ['nodelist','edgelist','num_nodes','num_edges', 'giulia_spatial_entropy','giulia_config_entropy','entropy_subtracted_baseline','runtime']

def get_table_download_link(df):
    
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() 
    href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
    return href
#    b64 = base64.b64encode(writer.encode()).decode() #Work around for your weird steps (the code above seems like it can be simplified)
#    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    
    
#'''Streamlit portion'''
uploaded_nodes = st.file_uploader("Upload your nodelist", type="CSV")
if uploaded_nodes is not None:
    nodelist = pd.read_csv(uploaded_nodes)
    nodelist.columns=['ens_id','expr_val']

uploaded_edges = st.file_uploader("Upload your edgelist", type="CSV")
if uploaded_edges is not None:
    edgelist = pd.read_csv(uploaded_edges)
    edgelist.columns=['source','target']


#creating a new csv file to write computed spatial entropy values and giving headers
fieldnames = ['nodelist','edgelist','num_nodes','num_edges', 'giulia_spatial_entropy','giulia_config_entropy','entropy_subtracted_baseline','runtime']

df=pd.DataFrame(columns=fieldnames)

if st.button('Generate Spatial Entropy'):
    myoutput=giulia_config_spatial_entropy(edgelist,nodelist)
    newdf = pd.DataFrame([myoutput])
    df=df.append(newdf)
    st.dataframe(df)
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    #get_table_download_link()
#'''End'''
