import streamlit as st

def app():
    st.title('About')

    st.write("This webapp allows researchers to calculate **network entropy** from any omic-based dataset. Network entropy provides an estimate of molecular \"disorder\" of a system, with a higher network entropy representing a probabilistically greater degree of disorganization or randomness in the system. ")
    st.write("This is published as a part of the manuscript **(eLife, under revision)**:  ")
    st.write("Link to manuscript DOI:[https://doi.org/10.1101/2020.07.22.207043](https://doi.org/10.1101/2020.07.22.207043)")
    st.write("**Pius, A., Clemens, Z., Sivakumar, S., Sahu, A., Shinde, S., Mamiya, H., ... & Ambrosio, F. (2020). The biphasic and age-dependent impact of Klotho on hallmarks of aging and skeletal muscle function. bioRxiv. ** ")
    st.text("")
    st.write("The mathematical basis for the network entropy calculation used in this study was first described by Menichetti. et. al.:")
    st.write("**Menichetti, G., Bianconi, G., Castellani, G., Giampieri, E., & Remondini, D. (2015). Multiscale characterization of ageing and cancer progression by a novel network entropy measure. Molecular BioSystems, 11(7), 1824-1831.**")
    st.text("")
    st.text("")

    st.write("Preprocessing includes generation of protein-protein interaction network from raw count matrix.")
    st.write("Example code for preprocessing is available on Github: `sruthi-hub/sarcopenia-network-entropy`")
    st.text("")
    st.text("") 

    st.text("Interpretation:")
    st.write("Whereas there is little information provided by the absolute value of network entropy generated, values become meaningful when comparing across samples or groups.") 
    st.write("Increasing entropy corresponds to increasing molecular disorder or increased flexibility of the system.")
    st.write("Decreasing entropy corresponds to decreasing molecular disorder or increased rigidity of the system.") 
    st.text("")
    st.text("") 
    st.text("") 

    st.write('Navigate to `Network entropy calculator` page to compute network entropy from your data!')


