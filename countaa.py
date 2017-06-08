# Rosalind-s-basic-problems
# http://rosalind.info/users/azizahma/

#!/usr/bin/env python
#Counting DNA Nucleotides 
def countaa(sequence):
    """Returns the number of amino acid occurrence in a sequence: A C G T"""
    A=sequence.count("A")
    C=sequence.count("C")
    G=sequence.count("G")
    T=sequence.count("T")
    print(str(A)+' '+str(C)+' '+str(G)+' '+str(T))
countaa("AATGCTTTCAATGGGAAAAAT")
