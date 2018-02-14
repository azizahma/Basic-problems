#Rearrangements Power Large-Scale Genomic Changes
#Point mutations - for single organism is like genome rearrangements for create & differentiate entire species
#gene_orders - like something to simplify comparison of two such genomes eg human vs mouse

import itertools
from functools import reduce
def gene_orders(n):
    '''The total number of permutations of length nn, followed by a list of all such permutations (in any order).'''
    l = list(range(0+1,n+1))
    nper = reduce(lambda m,n:m*n, l)
    #The number of permutations of a list is the factorial of the length of the list, divided by the product of the factorials of the multiplicity of each element (since sets of repeated elements are permuted with no effect)
    print(nper)
    for x in itertools.permutations(l,n):
        print(*x)

gene_orders(5)
