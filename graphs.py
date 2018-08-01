
import itertools

with open('rosalind_grph.txt') as f:
    d = ''.join([ line.strip() for line in f.read() ]).split('>')
    d = [ x for x in d if x is not '']
    d1 = [ x[:13] for x in d ]
    d2 = [ x[13:] for x in d ]
    comb = list(itertools.combinations(d1, 2))
    dct = dict(list(zip(d1, d2)))

def overlap(s1,s2,k):
    return s1[-k:] == s2[:k]

edges = []

for i, j in itertools.combinations(d1,2):
    idna, jdna = dct[i], dct[j]
    if overlap(idna,jdna,3):
         edges.append((i,j))
    if overlap(jdna, idna,3):
         edges.append((j,i))

for p in edges:
    print(p[0]+' '+p[1])
