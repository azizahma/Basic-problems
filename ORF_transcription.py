# Open Reading Frames
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

import re
import itertools

with open('input') as f:
    dct = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
            'TAT': 'Y', 'TAC': 'Y', 'TAA': 'stop', 'TAG': 'stop', 'TGT': 'C', 'TGC': 'C', 'TGA': 'stop', 'TGG': 'W',
            'CTT': 'L',
            'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
            'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
            'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N',
            'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V',
            'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D',
            'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    d = f.read().strip().replace('\n','')
    d = re.findall('[A,C,G,T]*', d)
    d = [ x for x in d if x is not '']
    d = ''.join(d)
    d_rev = [ x.replace('C','c').replace('G','C').replace('T','t').replace('A','T').replace('c','G').replace('t','A') for x in d ] # reverse complement
    d_rev = ''.join(d_rev)[::-1] # reverse complement

def ORF(seq):
    res = []
    start = [k for k, v in dct.items() if v == 'M']
    stop = [k for k, v in dct.items() if v == 'stop']
    for i in range(len(seq)):
        codon = seq[i:i+3]
        if codon == ''.join(start):
            for j in range(i+3,len(seq),3):
                a = seq[i:j]
                c = a[-3:]
                aa = [ v for k,v in dct.items() if k == c ]
                r =''.join(aa)
                res.append(r)
                if any(c==x for x in stop):
                    break
    res = ''.join(res).split('stop')[:-1]
    return res

results = [ORF(d), ORF(d_rev)]
print('\n'.join(set([ x for sub in results for x in sub ])))



