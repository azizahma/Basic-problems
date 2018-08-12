# Rearrangements Power Large-Scale Genomic Changes

import itertools
def permutations(file):
    """
    Given: A positive integer n≤7.
    Return: The total number of permutations of length n, followed by a list of all such permutations (in any order). 
    """
    with open(file) as f:
        d = int(f.read())
        n = [ x for x in range(1,d+1) ]
        results = list(itertools.permutations(n,d))
        print(len(results))
        for x in results:
            print(' '.join(str(y) for y in x))

permutations('rosalind_perm.txt')
