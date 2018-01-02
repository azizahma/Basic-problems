#Finding DNA strings that share some properties
#The adjacency list corresponding to O3. You may return edges in any order.
#Refer algorithm for DNA sequencing lectures: https://www.coursera.org/learn/dna-sequencing/lecture/lscgN/lecture-overlap-graphs

import re
#Define a function to return a dict from process of FASTA input
def clean_d(file):
    with open(file) as f:
        fr=f.read()
        frjoin=''.join([line.strip() for line in fr])
        frsplit = frjoin.split('>')
        cleanlist= [f for f in frsplit if f is not '']
    idx = []
    jseq = []
    for seq in cleanlist:
        i = re.findall('^''Rosalind_+\d*', seq)
        j = re.findall('[C,G,A,T]*', seq)
        idx.append(i)
        jseq.append(j)
    lidx = [y for x in idx for y in x]
    lseq = [y for x in jseq for y in x]
    lseq = [y for y in lseq if y is not '']
    d = dict(list(zip(lidx, lseq)))
    return d

#Define a function for directed overlaps of length k=3, between s1(suffix) and s2(prefix)
def overlap(s1,s2,k):
    return s1[-k:] == s2[:k]

#Define a function to look into combinations of (DNA) strings that match # tips: using itertools_combinations
import itertools
def k_edges(d,k):
    edges = []
    #edges2=[]
    for i, j in itertools.combinations(d,2):
        idna, jdna = d[i], d[j]
        #print(idna[-k:], jdna[:k])
        #print(idna,jdna)
        if overlap(idna,jdna,k):
            edges.append((i,j))
            #edges2.append((idna,jdna))

        if overlap(jdna, idna,k):
            edges.append((j,i))
            #edges2.append((jdna,idna))

    #return edges
    for p in edges:
        print(p[0]+' '+p[1])

print(clean_d('file'))
k_edges(clean_d('file'),3)

