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
        for v in locations:
            sv = s.replace(s[v[0]:v[0]+v[1]],'$'*v[1])
            s = sv
        dct = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
               'TAT': 'Y', 'TAC': 'Y', 'TAA': '', 'TAG': '', 'TGT': 'C', 'TGC': 'C', 'TGA': '', 'TGG': 'W',
               'CTT': 'L',
               'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
               'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
               'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N',
               'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V',
               'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D',
               'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
        exons = s.split('$')
        exons = ''.join([x for x in exons])
        for i in range(0, len(exons), 3):
            code = (exons[i:i + 3])
            print(''.join([ v for k,v in dct.items() if code==k ]), end='')

rna_splice('rosalind_splc.txt')
