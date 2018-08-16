# Genome Assembly as Shortest Superstring

import re
import itertools
def fragment_assembly(file):
    """
    Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent 
    reads deriving from the same strand of a single linear chromosome).
    The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire 
    chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
    Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome). 
    """
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        d = re.findall('[A,C,G,T]*', d)
        d = [ x for x in d if x is not '' ]
        min_l = int(len(d[0])/2)
        print(d)

        #results = []
        for x in d:
            for l in range(min_l, len(d[0])+1):
                for i in range(len(x)):
                    if len(x[i:i+l]) >= min_l:
                        pattern = x[i:i+l]
                        if any(sequence.find(pattern) >= 0 for sequence in [ y for y in d if y is not x ] ):
                            print(pattern)
                            print(x)
                            #results.append(pattern)
        #print(results)

fragment_assembly('input')

