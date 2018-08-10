# Open Reading Frames

import re
import itertools
def transcription(file):
    """
    Given: A DNA string s of length at most 1 kbp in FASTA format.
    Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
    """
    with open(file) as f:
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
        aa_seq = []
        for x in d:
            for i in range(0, len(x),3):
                dna = x[i:i+3]
                aa = ''.join([ v for k,v in dct.items() if k == dna ])
                aa_seq.append(aa)
        start = [ i for i,s in enumerate(aa_seq) if s == 'M']
        stop = [ i for i,s in enumerate(aa_seq) if s == 'stop' ][0]
        # use the approach of combining two numbers from start and stop lists
        l = []
        l.append(start)
        l.append([stop])
        for i,j in itertools.product(*l):
            if j > i:
                valid = aa_seq[i:j]
                print(''.join(valid))






transcription('input')