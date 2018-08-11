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
    aa = []
    start = [k for k, v in dct.items() if v == 'M']
    stop = [k for k, v in dct.items() if v == 'stop']
    
    for i in range(len(seq)):
        codon = seq[i:i+3]
        if codon == ''.join(start):
            for j in range(i+3,len(seq),3):
                a = seq[i:j]
                c = a[-3:]
                if any(c==x for x in stop):
                    print(a)
                    break







        # if code == 'ATG':
        #     aa.append(code)



    # aa = []
    # for i in range(0, len(seq),3):
    #     dna = seq[i:i+3]
    #     pr = ''.join([ v for k,v in dct.items() if k == dna ])
    #     aa.append(pr)
    # print(aa)


    #     start = [ i for i,s in enumerate(aa_seq) if s == 'M']
    #     stop = [ i for i,s in enumerate(aa_seq) if s == 'stop' ][0]
    #     # use the approach of combining two numbers from start and stop lists
    #     l = []
    #     l.append(start)
    #     l.append([stop])
    #     for i,j in itertools.product(*l):
    #         if j > i:
    #             valid = aa_seq[i:j]
    #             print(''.join(valid))
    #
    #     aa_seq_R = []
    #     for y in d:
    #         y = [ x.replace('C','c').replace('G','C').replace('T','t').replace('A','T').replace('c','G').replace('t','A') for x in y ] # reverse complement
    #         y = ''.join(y)[::-1]
    #         print(y)
    #
    #         for p in range(0, len(y), 3):
    #             dnaR = y[p:p+3]
    #             aaR = ''.join([v for k, v in dct.items() if k == dnaR])
    #             aa_seq_R.append(aaR)
    #
    #     print(aa_seq_R)
    #     start_rev = [i for i, s in enumerate(aa_seq_R) if s == 'M']
    #     stop_rev = [i for i, s in enumerate(aa_seq_R) if s == 'stop'][0]
    #     l_rev = []
    #     l_rev.append(start_rev)
    #     l_rev.append([stop_rev])
    #     print(l_rev)
    #     for p, q in itertools.product(*l_rev):
    #         if q > p:
    #             valid_rev = aa_seq_R[p:q]
    #             print(''.join(valid_rev))

ORF(d)