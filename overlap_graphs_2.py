#Overlap Graphs - O3

import itertools # to use combinations
def overlap_graphs_3(file):
    """
    Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
    Return: The adjacency list corresponding to O3. You may return edges in any order.
    """
    with open(file) as f:
        d = f.read().replace('\n','').split('>')
        d = [ x for x in d if x is not '' ]
        d1 = [ x[:13] for x in d ]
        print(d1)
        d2 = [ x[13:] for x in d ]
        comb = list(itertools.combinations(d1,2))
        print(comb)
        dct = dict(list(zip(d1,d2)))
        #comb = list(itertools.combinations(dct.keys(),2)) # itertools perhaps confused the use of combinations involving dct - so just do with the list

        for x in comb:
            r1,r2 = x
            s1 = ''.join([ v for k,v in dct.items() if r1==k ])
            s2 = ''.join([ v for k,v in dct.items() if r2==k ])
            #print(s1[:3], s1, s2[-3:], s2)
            #print(r1,s1,r2,s2)

            #if s1[-3:] == s2[:3] or s1[:3] == s2[-3:]:
            if s1[-3:] == s2[:3]:
                #print(x, s1, s2)
                print(' '.join(x))
            elif s1[:3] == s2[-3:]:
                #print(x, s1, s2)
                print(' '.join(x))

overlap_graphs_3('input')