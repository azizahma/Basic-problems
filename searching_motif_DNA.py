#Related to 'Finding a motif in DNA', this is 'Searching a motif in DNA strings'
#Return: A longest common substring of the collection.

import re
from Bio import SeqIO

def clean_v(file):
    with open(file) as f:
        fr = f.read()
        frjoin = ''.join([line.strip() for line in fr])
        frsplit = frjoin.split('>')
        cleanlist = [f for f in frsplit if f is not '']
        #print(len(cleanlist))
    idx = []
    jseq = []
    for seq in cleanlist:
        i = re.findall('^''Rosalind_+\d*', seq)
        j = re.findall('[C,G,A,T]*', seq)
        idx.append(i)
        jseq.append(j)
    lidx = [y for x in idx for y in x] #to make one list rather than data in list of lists, so the list comprehension z for z in lseq if z is not '', works
    lseq = [y for x in jseq for y in x]
    lseq = [z for z in lseq if z is not '']
    #d = dict(list(zip(lidx,lseq)))
    return lseq

#print(clean_v('file'))

l = list(clean_v('file'))
short = min([x for x in l])
other = [x for x in l if x is not short]
short_len = min([len(x) for x in l])#to look for motifs in the shortest sequence
motif = ''
for i in range(short_len):
    for j in range(i, short_len):
        mot = short[i:j+1]
        f = False
        for c in other:
            if mot in c:
                f = True
            else:
                f = False
                break
        if f and len(mot) > len(motif):
            motif = mot

print(motif)














