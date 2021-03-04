import streamlit as st

def app():
    st.title('About')

    st.write("This webapp allows researchers to calculate network entropy from any omic-based dataset.")
    st.write("This is published as a part of the manuscript: The biphasic and age-dependent impact of Klotho on hallmarks of aging and skeletal muscle function")
    st.text("")
    st.write("Preprocessing includes generation of protein-protein interaction network from raw count matrix.")
    st.write("Example code for preprocessing is available on Github: `sruthi-hub/sarcopenia-network-entropy`")
    st.text("")
    st.text("Interpretation:")
    st.write("This value becomes meaningful when one wants to compare across samples.") 
    st.write("Increasing entropy corresponds to increasing molecular disorder or increased flexibility of the system.")
    st.write("Decreasing entropy corresponds to decreasing molecular disorder or increased rigidity of the system.") 
    st.text("")
    st.text("") 
    st.write("We acknowledge Menichetti. et. al. for developing the mathematical basis for network entropy calculation.")
    st.write("Menichetti, G., Bianconi, G., Castellani, G., Giampieri, E., & Remondini, D. (2015). Multiscale characterization of ageing and cancer progression by a novel network entropy measure. Molecular BioSystems, 11(7), 1824-1831.")
    st.text("")
    st.text("")


    st.write('Navigate to `Network entropy calculator` page to compute network entropy from your data')


