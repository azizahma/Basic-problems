# Locating Restriction Sites - The Billion-Year War

import re
def reverse_palindrome(file):
    """
    Given: A DNA string of length at most 1 kbp in FASTA format.
    Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may 
    return these pairs in any order.
    """
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        d = re.findall('[A,C,G,T]*',d)
        d = ''.join([ x for x in d if x is not ''])

        for i in range(len(d)+1):
            for l in range(4,13):
                seq = d[i:i+l]
                if len(seq) >= 4:
                    seqr = seq.replace('G','g').replace('C','G').replace('A','a').replace('T','A').replace('g','C').replace('a','T')[::-1]
                    if seq == seqr and i+l <= len(d):
                        print(i+1, l)

reverse_palindrome('rosalind_revp.txt')