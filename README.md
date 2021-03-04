# Network entropy calculator - streamlit app
Network entropy calculator based on omic-based datasets.

# How to Run

1. Follow preprocessing steps from example sruthi-hub/sarcopenia-network-entropy

This example shows how to map raw transcriptomic counts to generate protein-protein interaction network.

2. Create nodelists and edgelists

For bulk RNA-seq data, one sample (or animal) would have one nodelist and one edgelist. 

3. Upload nodelist and edgelist and interpretation of network entropy

Network entropy value can be extracted from the CSV file output from the webapp. 
This value becomes meaningful when one wants to compare across samples. 
Increasing entropy corresponds to increasing molecular disorder or increased flexibility of the system.
Decreasing entropy corresponds to decreasing molecular disorder or increased rigidity of the system. 


# More information:
Please refer to the following papers for more details on implementation and interpretation:

1. https://pubs.rsc.org/en/content/getauthorversionpdf/c5mb00143a
Menichetti, G., Bianconi, G., Castellani, G., Giampieri, E., & Remondini, D. (2015). Multiscale characterization of ageing and cancer progression by a novel network entropy measure. Molecular BioSystems, 11(7), 1824-1831.

2. Under review at eLife
The biphasic and age-dependent impact of Klotho on hallmarks of aging and skeletal muscle function
Abish Pius, Zachary Clemens, Sruthi Sivakumar, Amrita Sahu, Sunita Shinde, Hikaru Mamiya, Nathaniel Luketich, Jian Cui, Joerg D. Hoeck, Sebastian Kreuz, Michael Franti, Aaron Barchowsky, Fabrisia Ambrosio
bioRxiv 2020.07.22.207043; doi: https://doi.org/10.1101/2020.07.22.207043

