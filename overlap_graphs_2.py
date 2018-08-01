#Overlap Graphs - O3

import itertools # to use combinations
def overlap_graphs_3(file):
    """
    Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
    Return: The adjacency list corresponding to O3. You may return edges in any order.
    """

    with open(file) as f:
        d = ''.join([line.strip() for line in f.read()]).split('>')
        d = [x for x in d if x is not '']
        d1 = [x[:13] for x in d]
        d2 = [x[13:] for x in d]
        comb = list(itertools.combinations(d1, 2))
        dct = dict(list(zip(d1, d2)))

        for x in comb:
            r1, r2 = x
            s1 = ''.join([v for k, v in dct.items() if r1 == k])
            s2 = ''.join([v for k, v in dct.items() if r2 == k])
            if s1[::-1][:3] == s2[:3]:
                print(' '.join(x))
            elif s2[::-1][:3] == s1[:3]:
                print(' '.join(x))

overlap_graphs_3('rosalind_grph.txt')


overlap_graphs_3('input')