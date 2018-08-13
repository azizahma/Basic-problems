# Genes are Discontiguous

import re
def rna_splice(file):
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        d = re.findall('[A,C,G,T]*', d)
        d = [ x for x in d if x is not '' ]
        print(d)

rna_splice('input')