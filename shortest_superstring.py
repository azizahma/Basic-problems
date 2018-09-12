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
    o_lap = {}
    for lname in [ k for k,v in dct.items() ]:
        a = {lname:{}}
        zz = {}
        for rname in [ k for k,v in dct.items() if k is not lname ]:
            left = ''.join([v for k, v in dct.items() if k == lname])
            right = ''.join([v for k, v in dct.items() if k == rname ])
            b = {rname:overlap(left,right)}
            zz.update(b)
        a[lname] = zz
        o_lap.update(a)
    return o_lap

import pandas as pd
def prettify_o_lap(o_lap):
    df = pd.DataFrame(o_lap)
    df = df.fillna('-')
    return df
    #print(df.fillna('-'))

def find_first_read(o_lap): # via dictionary
    t = [ [ j for i,j in v.items() if j is not 0 ] for k,v in o_lap.items() ]
    m = max([ len(x) for x in t ])
    ext = [ {k:[ j for i,j in v.items() if j is not 0 ]} for k,v in o_lap.items() ]
    for x in ext:
        print(''.join([ k for k,v in x.items() if len(v)==m ]))

o_lap = get_all_o_lap(dct)
#print(o_lap)
#prettify_o_lap(o_lap)
find_first_read(o_lap)

