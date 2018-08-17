# Genome Assembly as Shortest Superstring

# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
# reads deriving from the same strand of a single linear chromosome).
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
# chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).


import re
import itertools

with open('input') as f:
    d = f.read().strip().replace('\n','')
    dk = re.findall('Rosalind_[0-9]*', d)
    dv = re.findall('[A,C,G,T]*', d)
    dv = [ x for x in dv if x is not '' ]
    dct = dict(list(zip(dk,dv)))
    length = int(sum([ len(x) for x in dv ])/len(dk))

def overlap(dct):
    pairs = list(itertools.permutations([k for k,v in dct.items()],2))
    for p in pairs:
        left = ''.join([ v for k,v in dct.items() if k == p[0] ])
        right = ''.join([ v for k,v in dct.items() if k == p[1] ])
        for i in range(length,0,-1):
            l = left[i:]
            r = right[:-i]
            if l == r:
                print(l,r)
overlap(dct)
