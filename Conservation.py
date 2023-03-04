import pandas as pd
import numpy as np

# Obtain the multiple sequence alignment, and turn to array
MSA_df = pd.read_csv('C:/Users/LNH/Desktop/Study/Comparative/Comparative Genomics/Assignment/align_homologs', sep="\t", header=None, skiprows=1)
MSA = np.array(MSA_df)

# First of all, we need to delete all useless information before sequence, which means to 
# delete 36 positions in each line
# then, we need to remove all lines that do not contain sequence
remove = []
for i in range(len(MSA)):
    MSA[i, 0] = MSA[i, 0][36:]
    if '.' in MSA[i, 0] or ':' in MSA[i, 0] or '*' in MSA[i, 0]:
        remove.append(i)
i = 0
for j in range(len(remove)):
   MSA = np.delete(MSA, remove[j] - i, axis=0)
   i = i + 1

# In this research, we have 72 different protein sequences, MSA divides them into 13 regions,
# the last region contains 29 sites, and each of the rest contians 50 sites
proteins = 72
region_sites = len(MSA[1, 0])
last_regoin_sites = len(MSA[-1, 0])
regions = len(MSA)//proteins
columns = (regions - 1) * region_sites + last_regoin_sites
# We create a empty list with 936 rows and 50 columns
seq = np.empty((len(MSA), region_sites), dtype=str)

# For convenience, we add "1" to fill in the last region, so each region has 50 sites
for i in range(len(MSA) - proteins, len(MSA)):
    for j in range(region_sites - last_regoin_sites):
        MSA[i, 0] = MSA[i, 0] + "1"

# We move every site from MSA to the list 'seq', so each element in the 'seq' represents one 
# site on the sequence
for i in range(len(MSA)):
    for j in range(region_sites):
        seq[i, j] = list(MSA[i, 0])[j]

# We reshape the seq, now we have 13 regions like MSA result, each region has 72 rows 
# (protein) and 50 columns(sites)
seq.shape = (regions, proteins, region_sites)
print(seq)

# Now we calculate varibality for each position
# Be careful! The position contain "1" should be ignored!
# We put all varibalities into one list 'Vs'
Vs = []
for i in range(regions):
    for j in range(region_sites):
        if seq[i][0][j] != "1":
            eachSite = []
            for m in range(proteins):
                eachSite.append(seq[i][m][j])
            n = 1
            for e in eachSite:
                if e != '-' and eachSite.count(e) > n:
                    max = e
                    n = eachSite.count(e)
            k = len(set(eachSite))
            N = proteins
            Variability = k * N / n
            Vs.append(Variability)

# Print all sites that has variability equal to 1, which means that amino acid conserved in all 
# protwins
for i in range(len(Vs)):
    if Vs[i] == 1:
        print(i)
        print(seq[i//region_sites][0][i%regions])


# Create csv file for variablity, and we can plot the values in R
Vs_df = pd.DataFrame(data=Vs)
Vs_df.to_csv('C:/Users/LNH/Desktop/Study/Comparative/Comparative Genomics/Assignment/Variability.txt', encoding = 'gbk', header=None)
