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

#left = dv[1]
#right = dv[3]
print(dct)

def overlap(left, right):
    for i in range(length,0,-1):
        l = left[i:]
        r = right[:-i]
        if l == r : #######and len(l) >= 5:
            a = {left:{right:len(l)}}
        else:
            a = {left:{right:0}}
        print(a)
## I think the seq name must be specify in overlap not in get_all_o_lap

def get_all_o_lap(dct):
    for l in list(itertools.permutations([k for k,v in dct.items()],2)):
        left = ''.join([v for k, v in dct.items() if k == l[0]])
        right = ''.join([ v for k,v in dct.items() if k == l[1]])
        overlap(left,right)



# dd = {}
# for l in list(itertools.permutations(dk,2)):
#     left = ''.join([ v for k,v in dct.items() if k == l[0]])
#     right = ''.join([ v for k,v in dct.items() if k == l[1]])
#     if overlap(left,right) is not None:
#         a = {l:overlap(left,right)}
#         dd.update(a)
# print(dd)

#overlap(left,right)
get_all_o_lap(dct)
