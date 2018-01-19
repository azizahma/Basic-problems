#Checking modulo relationship

def modulo_relationship(a,b,c,d):
    n = 11
    if a % n == b % n:
        print('a = b mod n')
    else:
        print('False')
    if c % n == d % n:
        print('c = d mod n')
    else:
        print('False')
    if (a+c) % n == (b+d) % n:
        print('a+c = b+d mod n')
    else:
        print('False')
    if (a*c) % n == (b*d) % n:
        print('a*c = b*d mod n')
    else:
        print('False')

#modulo_relationship(29, 73, 10, 32)
#modulo_relationship(10,15,27,90)

#Pitfalls of reversing translation
#The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
def reverse_translation(file):
    '''#The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)'''
    from functools import reduce
    with open(file) as f:
        pr = ' '.join(line.strip() for line in f)
        dct = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
               'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '', 'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W', 'CUU': 'L',
               'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H',
               'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I',
               'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N',
               'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V',
               'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D',
               'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

        lstop = [len([ k for (k,v) in dct.items() if v == '' ])]

        nRNA = []
        for aa in pr:
            rna = [ k for (k,v) in dct.items() if v == aa ]
            #dd = { aa: len(rna) }
            nRNA.append(len(rna))

        nRNA = nRNA + lstop
        #print(nRNA)
        n = reduce(lambda x,y : x*y, nRNA)
        return n % 1000000

print(reverse_translation('file'))
