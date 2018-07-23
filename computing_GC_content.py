__author__ = 'azizah'

#Computing GC content - identifying unknown DNA quickly

def reading_fasta(file):
    key = []
    val = []
    with open(file) as f:
        seq = f.read().replace('\n','').split('>')
        seqc = [ x for x in seq if x is not '']
        for x in seqc:
            key.append(x[:13])
            val.append(x[13:])
    return key, val

key, val = reading_fasta('rosalind_gc.txt')

import numpy as np
def computing_highest_GC(k,v):
    dct = dict(list(zip(k,v)))
    percentage = dict({(k,((v.count('G')+v.count('C'))*100/len(v))) for k,v in dct.items()})
    for k,v in percentage.items():
        if v == max(percentage.values()):
            print(k+'\n'+str(np.abs(v)))

computing_highest_GC(key, val)



