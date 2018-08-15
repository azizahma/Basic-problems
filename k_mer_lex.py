# Enumerating k-mers Lexicographically

import itertools
def organising_strings(file):
    """
    Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).
    Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard 
    order of symbols in the English alphabet).
    """
    with open(file) as f:
        d = f.readlines()
        d = [ x.replace('\n','') for x in d ]
        a = d[0].replace(' ','')
        res = list(itertools.permutations(a,int(d[1])))

        for x in res:
             print(''.join(x))

organising_strings('input')
#organising_strings('rosalind_lexf.txt')