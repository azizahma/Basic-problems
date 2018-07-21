#Complementing the stand of DNA

def reverse_complement(file):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    """
    with open(file) as f:
        r = f.read().replace('\n','')[::-1] #[begin:end:step]
        dct = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        r = [x for x in r]
        r_dna = []
        for rr in r:
            r_dna.append([v for k,v in dct.items() if rr == k])
        for nuc in r_dna:
            print(''.join(nuc), end='') #set an end to a print statement

reverse_complement('rosalind_revc.txt')