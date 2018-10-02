# Genome Assembly as Shortest Superstring

# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
# reads deriving from the same strand of a single linear chromosome).
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
# chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome)

# References:
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

def find_first_read(o_lap): # via dict; based on 'it only has a good overlap (>5 is significant overlap) when positioned to the left of other reads'
    '''to look for - 'which row/column has no 'significant' overlap? (df changes row and column - 
    via dictionary method'''

    results = []
    for k,v in o_lap.items():
        for i,j in v.items():
            if j < 5: #
                #results.append((k,i)) # checking purpose
                results.append(i)

    results = dict( (x,results.count(x)) for x in set(results) )
    m = max([ v for k,v in results.items() ])
    first = ''.join([ k for k,v in results.items() if v == m ])
    return first

def find_key_for_largest_value(dic):
    # print(dic) # imagine a dict from any left (or first) read ie. { k:v for k,v in o_lap.items() if k == 'Rosalind_56' }
    m = [ [j for i,j in v.items() ] for k,v in dic.items()]
    m = max(m[0])
    largest = [ [ i for i,j in v.items() if j == m ] for k,v in dic.items() ]
    return ''.join(largest[0])

def find_order(first, o_lap):
    '''Returns a list of read names in the order in which they represent the genomic sequence.'''
    # dic = {k:v for k,v in o_lap.items() if k == first} # must be called after first is obtained
    if max([[j for i, j in v.items()] for k, v in o_lap.items() if k == first][0]) < 3:
        return first
    else:
        next_r = find_key_for_largest_value({k:v for k, v in o_lap.items() if k == first})
        return [first] + [find_order(next_r, o_lap)]

def assemble_G(order, dct, o_lap):
    seq = ''
    for i in range(len(order)-1):
        p = ''.join([k for k,v in dct.items() if k==order[i]])
        n = ''.join([k for k,v in dct.items() if k==order[i+1]])
        p_seq = ''.join([v for k, v in dct.items() if k == order[i]])
        n_seq = ''.join([v for k,v in dct.items() if k==order[i+1]])
        n_olap = [[j for i,j in v.items() if i==n] for k,v in o_lap.items() if k==p]
        l = n_olap[0][0]
        s = p_seq+n_seq[l:]
        seq += s

        
        print(seq)


    #l = order[-1]


o_lap = get_all_o_lap(dct)
first = find_first_read(o_lap)
dic = {k:v for k, v in o_lap.items() if k == first}
largest = find_key_for_largest_value(dic)
#order = find_order(first, o_lap)
order = re.findall('Rosalind_[0-9]*', str(find_order(first, o_lap)))

print(order)
assemble_G(order, dct, o_lap)

# print(order)
# print(dct)
# print(first)
# print(o_lap)
# print(largest)
# print(prettify_o_lap(o_lap))


