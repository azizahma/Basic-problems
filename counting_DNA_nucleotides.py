#Counting the number of each nucleotide in a sequence

def count_CGAT(file):
    """
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    with open(file) as f:
        dna = f.read().replace('\n','')
        key = [x for x in dna]
        val = [key.count(x) for x in key]
        d = dict(list(zip(key,val)))
        for k,v in sorted(d.items()):
            print(str(v)+ ' ', end='')

count_CGAT('rosalind_dna.txt')