# Genome Assembly as Shortest Superstring

import re
import itertools
def fragment_assembly(file):
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        #dR = re.findall('Rosalind_[0-9]*', d)
        d1 = re.findall('[A,C,G,T]*', d)
        d1 = [ x for x in d1 if x is not '' ]
        #dct = dict(list(zip(dR,d1)))
        #print(list(itertools.permutations(dR,2)))
        print(d1)
        for x in d1:
            print(x)

fragment_assembly('input')

