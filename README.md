# Comparative_genomics
1.	Introduction 
In this study, Prosthecochloris aestuarii and Rubrobacter xylanophilus were subjected to comparative genomic analysis. Orthologs were found between protein sequences from two different species using the Best Bidirectional Hits (BBH) method, and a phylogenetic tree was created by aligning the homologs of one example of orthologs. Speciation and Duplication events were marked on the tree, which was compared with a species tree based on rRNA resources. Multiple Sequences Alignment (MSA) was applied in the end to identify conserved regions in protein sequences and potential promotor regions in DNA sequences.

2. Methods 
2.1 Compute orthologs using Best Bidirectional Hits
All protein sequences of Prosthecochloris aestuarii (RefSeq: GCF_000020625.1) and Rubrobacter xylanophilus (RefSeq: GCF_000014185.1) were downloaded from NCBI database (https://www.ncbi.nlm.nih.gov/data-hub/genome/) as FASTA files. Two FASTA files were used to build a database of Prosthecochloris aestuarii and a database of Rubrobacter xylanophilus, then protein sequences from one species were used to run protein blast with the database of another species’ protein sequences and the database of its own protein sequences. Four output files were generated from protein blast (output_Pa.txt, output_Pa_self.txt, output_Rx.txt, ouput_Rx_self.txt), and a python script (BBH.py) was created to generate BBH for two species using these output files, and it also indicated all in-paralogs.

2.2 Check orthology with a phylogenetic tree
One protein sequence of orthologs from co-orthology was picked to run protein blast in NCBI with standard databse and retrieve homologs to that protein sequence, then these homologs and the BBH were used to do MSA and generate the phylogenetic tree using clastalw2. When building the tree in clastalw2, the function of excluding positions with gaps and correcting for multiple substitutions was turned on, and the bootstrap value was set as 1000. The tree file was visualized in iTol (http://itol.embl.de) including branch lengths and bootstrap values, and speciation events were marked as red squares and duplication events were marked as green squares. In addition, rRNA sequences of all homologs species were downloaded from silva rRNA database (https://www.arb-silva.de/), and a species tree was built using these rRNA sequences. The species tree was also visualized in iTol to discuss the differences from the phylogenetic tree of homologs.

2.3 Identify functional regions
The resulting file of MSA was used to run a python script (Conservation.py), which uses an algorithm to calculate the variability to measure conservation and results in a list of variabilities to every position in the sequence (Variability.txt). The list of variability was exploited to generate a variability plot in R, and the value of variability is equal to 1 means all sequences share the same amino acid in that position.
variability=(N*k)/n
N: The number of sequences in the alignment
k: The number of different amino acids at a given position
n: The frequency of the most common amino acid at that position

2.4 Identify promotor regions
In order to identify promotor regions, the DNA sequences to specific proteins (orthologs) were downloaded from the NCBI and moved to one FASTA file. Clastalw2 was used to do the MSA analysis of these DNA sequences, and PVS (http://imed.med.ucm.es/PVS/) was used to see the variability plot.

