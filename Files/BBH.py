import pandas as pd
import numpy as np

BBH = {}
inparalogs = {}

# Create arrays for four different protein BLAST results
# output_Pa.txt: protein BLAST of protein sequences of Prosthecochloris aestuarii, database is protein sequences of Rubrobacter xylanophilus
# output_Rx.txt: protein BLAST of protein sequences of Rubrobacter xylanophilus, database is protein sequences of Prosthecochloris aestuarii
# output_Pa_self.txt: protein BLAST of protein sequences of Prosthecochloris aestuarii, database is protein sequences of Prosthecochloris aestuarii
# output_Rx_self.txt: protein BLAST of protein sequences of Rubrobacter xylanophilus, database is protein sequences of Rubrobacter xylanophilus
# In these four arrays, 1st column is the query name, 2nd column is the target name, 3rd column is the coverage rate, 4th column is the evalue
pa_df = pd.read_csv('D:/blast-BLAST_VERSION+/bin/output_Pa.txt', sep="\t", header=None)
pa_protein_hits = np.array(pa_df.iloc[:, [0, 1, 2, 10]])
print(len(pa_protein_hits))

rx_df = pd.read_csv('D:/blast-BLAST_VERSION+/bin/output_Rx.txt', sep="\t", header=None)
rx_protein_hits = np.array(rx_df.iloc[:, [0, 1, 2, 10]])
print(len(rx_protein_hits))

pa_self_df = pd.read_csv('D:/blast-BLAST_VERSION+/bin/output_Pa_self.txt', sep="\t", header=None)
pa_self_protein_hits = np.array(pa_self_df.iloc[:, [0, 1, 2, 10]])
print(len(pa_self_protein_hits))

rx_self_df = pd.read_csv('D:/blast-BLAST_VERSION+/bin/output_Rx_self.txt', sep="\t", header=None)
rx_self_protein_hits = np.array(rx_self_df.iloc[:, [0, 1, 2, 10]])
print(len(rx_self_protein_hits))

# For each protein sequence that finds the best hit in output_Pa.txt, check if each sequence has the in-paralogs
for i in range(len(pa_protein_hits)):
    protein = pa_protein_hits[i, 0]
    BH = pa_protein_hits[i, 1]
    evalue = pa_protein_hits[i, 3]

    # For each protein sequence that finds the best hit in output_Rx.txt, check if that sequence is the BH and if the BH of this sequence is the protein
    for m in range(len(rx_protein_hits)):
        if rx_protein_hits[m, 0] == BH and rx_protein_hits[m, 1] == protein:
            BBH[protein] = BH  # Now we have find one pair of BBH, and the next is to check if there exists inparalogs
            # First check if rx_protein has an inparalogs
            rxprotein = rx_protein_hits[m, 0]
            rxevalue = rx_protein_hits[m, 3]
            for n in range(len(rx_self_protein_hits)):
                # If two sequences from one species are more similar to each other than any sequence in the other specie, this sequence has inparalogs
                # , and both sequences are orthologous to the BBH
                if rx_self_protein_hits[n, 0] == rxprotein and rx_self_protein_hits[n, 2] != 100 and rx_self_protein_hits[n, 3] < rxevalue:
                    rxinparalogs = rx_self_protein_hits[n, 1]
                    inparalogs[rxprotein] = rxinparalogs

            # Then check if pa_protein has inparalogs
            for j in range(len(pa_self_protein_hits)):
                # If two sequences from one species are more similar to each other than any sequence in the other specie, this sequence has an inparalogs
                # , and both sequences are orthologous to the BBH
                if pa_self_protein_hits[j, 0] == protein and pa_self_protein_hits[j, 2] != 100 and pa_self_protein_hits[j, 3] < evalue:
                    painparalogs = pa_self_protein_hits[j, 1]
                    inparalogs[protein] = painparalogs

print("The number of BBH pairs:", len(BBH))
print("The number of inparalogs:", len(inparalogs))
print("The number of orthologs:", len(BBH) * 2 + len(inparalogs))







