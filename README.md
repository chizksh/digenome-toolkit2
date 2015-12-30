# Digenome-toolkit ver2.

We use Cas9 nuclease-digested whole genome (digenome) sequencing (Digenome-Seq) to profile genome-wide Cas9 off-target effects in cells. We can identify off-target mutations induced by programmable nucleases in a bulk population of cells by sequencing nuclease-digested genomes (digenomes). It should be possible to cleave off-target DNA sequences efficiently at high RGEN concentration in vitro, producing many DNA fragments with identical 5’ ends. These RGEN-cleaved DNA fragments would produce sequence reads that are vertically aligned at nuclease cleavage sites. In contrast, all other sequence reads would be aligned in a staggered manner. A computer program can be developed to search for sequence reads with straight alignment that correspond to off-target sites.
We updated Digenome-seq tool kit by scoring system.

Instructions

1.In order to find start/end positions of aligned sequences,  1.find_position_bam.cpp  needs to be compiled into binary. By running  build_find_position_bam.sh , it will firstly automatically download and compile bamtools library (https://github.com/pezmaster31/bamtools) and secondly compile  1.find_position_bam.cpp  into binary. To build bamtools library properly, cmake, g++, and git should be pre-installed.


2.Set an environment variable 'DIGENOME_HOME', to the directory which contains python files and executables.


3.Copy digenome-run script to bin directory (i.e. ~/bin), and run the script to analyze BAM file, as below:


digenome-run [-r cutoff_ratio=20.0] [-g difference=1] BAM_PATH [step=1]

It will automatically execute all required processes. It needs 'pysam' python package and 'pypy' to run properly.
