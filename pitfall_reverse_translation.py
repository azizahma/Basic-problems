#Pitfalls of Reversing Translation - more than one codons would translate into a single amino acid residue.

from functools import reduce
def pitfall_r_translation(file):
    """
    Given: A protein string of length at most 1000 aa.
    Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
    (Don't neglect the importance of the stop codon in protein translation.)
    """

    dct = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
               'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '', 'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W', 'CUU': 'L',
               'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H',
               'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I',
               'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N',
               'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V',
               'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D',
               'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

    with open(file) as f:
        stop = len([k for k, v in dct.items() if v == ''])
        rna = []
        for x in f.read():
            r = [ k for k,v in dct.items() if v == x ]
            rna.append(r)
        rna = [ x for x in rna if x != []]
        return (reduce(lambda i,j: i*j, [len(x) for x in rna]) * stop) % 1000000 # return only modulo

print(pitfall_r_translation('rosalind_mrna.txt'))