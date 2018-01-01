#Identifying Unknown DNA Quickly - Computing GC Content
#The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
import re
import numpy as np
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

#print(clean_d('file'))

idx=[]
vals=[]
for k, v in clean_d('file').items():
    #print(k,v)
    h = len(v)
    t = v.count('G')+v.count('C')
    percent = (t*100)/h
    idx.append(k)
    vals.append(percent)
dd = dict(list(zip(idx,vals)))
m = [ k for k,v in dd.items() if v == max(dd.values())]
n = [v for k,v in dd.items() if v == max(dd.values())]
print(''.join(m))
nn = np.abs(n)
#print(''.join(map(str, nn)))# works for a list with more than one element
print(str(nn).strip('[]'))
