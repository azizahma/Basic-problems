# Genes are Discontiguous

import re
def rna_splice(file):
    """
    Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
    Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.) 
    """
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        d = re.findall('[A,C,G,T]*', d)
        d = [ x for x in d if x is not '' ]
        s = ''.join(d[0])
        introns = d[1:]
        length = [ len(x) for x in introns ]
        locations = []
        for l in length:
            for i in range(len(s)):
                ss = s[i:i+l]
                if any(ss==intr for intr in introns):
                    locations.append((i,l))
        exons = []
        for v in locations:
            exon1 = s[:v[0]]
            exon2 = s[v[0]+v[1]:]
            exons.append(exon1+exon2)
        # the last exons to translate
        


rna_splice('input')