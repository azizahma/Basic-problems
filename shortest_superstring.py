# Genome Assembly as Shortest Superstring

# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
# reads deriving from the same strand of a single linear chromosome).
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
# chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome)

# https://munch-lab.org/2013/11/29/exercise-genome-assembly/
# https://www.coursera.org/lecture/dna-sequencing/lecture-the-shortest-common-superstring-problem-NAXB5

import re
import itertools

with open('input') as f:
    d = f.read().strip().replace('\n','')
    dk = re.findall('Rosalind_[0-9]*', d)
    dv = re.findall('[A,C,G,T]*', d)
    dv = [ x for x in dv if x is not '' ]
    dct = dict(list(zip(dk,dv)))
    length = int(sum([ len(x) for x in dv ])/len(dk))

left = dv[0]
right = dv[2]

def overlap(left, right):
    results = []
    for i in range(length,0,-1):
        l = left[i:]
        r = right[:-i]
        if l == r: #and len(l) >= 5:
            results.append(len(l))
        else:
            results.append(0)
    return max(results)

def get_all_o_lap(dct):
    for lname in [ k for k,v in dct.items() ]:
        a = {lname:{}}
        zz = {}
        for rname in [ k for k,v in dct.items() if k is not lname ]:
            left = ''.join([v for k, v in dct.items() if k == lname])
            right = ''.join([v for k, v in dct.items() if k == rname ])
            print(left,right)
            b = {rname:overlap(left,right)}
            zz.update(b)
        a[lname] = zz
        print(a)

#overlap(left,right)
get_all_o_lap(dct)

