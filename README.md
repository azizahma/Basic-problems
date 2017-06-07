# Rosalind-s-basic-problems
http://rosalind.info/users/azizahma/

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

#!/usr/bin/env python
# Counting point mutation
def hamming(sequence1, sequence2):
    """Returns Hamming score of two same length aligned amino acid sequences that differs"""
    seqval1=list(sequence1)
    seqval2=list(sequence2)
    compare_seqval=[(seqval1==seqval2) for seqval1, seqval2 in zip(seqval1,seqval2)]
    hamming_score=compare_seqval.count(False)
    print(hamming_score)

sequence1='GGCGCATGCACATCTCAGGGCTGAGTATCAATACATCCCGATTGAACTAGATCAGAACTTGACTTTTTTACCCCTGATCGTGAATGGCTTACATCTTTAGCGCTAATTCTCCGCGTTATCATTGCCTTCATACGATTAACTGCCATCTTTCAATTATACAGTAGATCGACTATTGGGTAACTATGGGGCATACCCTCACTCTTGAAGCCATTCCTCGCAGCGGAGTTCGCCGTCATGATTCCCATTCATCAGCGAGATTCTCTACCGGCAGAACCCGCACCGTTCCAAAATGACCAACCTAACGGTTCGTGGACTGAAGTACAACCTTTATGGGAGTGAACTACTAACGAGCCTTTCTTAATTGAGCGACCCTGTCAGTGGTCGATATCCCTGGACCGAAGGACAGAACAATATCATTACGGCGGCTAATACAGAGTTTCCGTTCCCGACGCTCGTTCCAAGCTGGCTAGATGCTATATTGCAGGTCCGCGCTCGTAAAGGCTATATAGTTCCATTATTACTAACCTGCCTCCTCCAAAACTGTTTAGCTACCTACTACGCTTTAAATGAGATCCTTTGCAGCCCTCCACTCTCTCCGAAGTAAGCAGGGGATCGTATTAGCAATACATCTGTGGTTGCGGCACGCTGCATGCCGATCACCTTGCAGAACCGTGCCTTCCACTACTGCATCTAGGAACTATACTGGCTCTGGCGTAGAATTGGCAATGTAAGGCGCCAGCCGGCACGTGAGAAAAAATATTCAGCATCCATCATTGGGACAGATATCAGGTCAGCACCTTGACGAAAAGTCCCGGTTCCGTATTAGTGCCTATAGGAGGATGATGCCAAACGCAGGTAGCAAAGCTGTAGATCAACTAAGGAGCTGGTCTGGAACAAAATTAGCTGCAGTTAAACTGTAAATTCATCTATGGGTCAATCGACTGTTAGTGTTGTATACCTTACAAGAGCACTAAAGCGGATGAGGAGTTGGCAAAACT'
sequence2='TGCACGAGAGCGTGTCAGGCTTCGATCACTAAACGTCGTGATACAGTTCCGTCTTAACTGTGCGGTCTAACATCCGATCCTTATTTCGCGACATTTTTCGGGAGAACGGAAGCCATCCTATTAGATCTGCTGCTATCTACTATGACCTTGCAACTATACCTTGAAACGCGTGTGAGAGAAGTCGATGGAACATCCTCATTCCTGTATTAATCGCCCGGTGAAGAGATCGATCGCATGATTATCTTTCAACGATTAGGTTAAGCAGTCGCACAACCCAGCCTCTTACAAACTGACCTAGCAATGAGCTATACAATTGAAACAAGCGCTTTATAACACTGACCCTCGCCTAATCATGCCTGCATCAGGCTATTCATTCCGTGGTGAAGTGACCAGGATATCCATACAATTCAATATGACCTAGGCGTCAACTATCGAAATACTGGGCTCGACGCATACGCATGGCGCCCGGGTTTCTCGTCTGAAAATCCCCGCTCAGAGCGTTTACGAATCTACGGTATCGCTAACGACTATCGGTCGAAAATGATTCTAGGACGATCACGCAGTGACGGATGTCCTTTACAGCCCAGCACTCAGCCCTCTGTACTTTGCGCACTTGATTAGAGATTCGTTGTGATGAACTGAACCCTTGCCAATAGTACACATTCACAGCCGGGCCGTCCTCATCAATATTGAGGACATATTTTCGACCATGTGTTTGGTTCGGAACGACAAACATCAACCAGGAAATCATACGAAGCACGGCGCATCAGTCATAGGCGCAGGCATACCGGATACACGTTTGCGAAAACTCCCAGCTCGCTTTTCCTCCATTGGGGAAGAAGGGAACAACCCCAATTAGCAACACCCTGCTTCAGATAAAGACCTGGTGTGTGGAAAGACTATCCGGGTAAACCTAGAAATGACAACGCTGGCATAACTTCGGGATAGGATTTTTATGTCTGTAAGGCCACAAAGGCGGTTTATCACGTTCGATTAGT'
hamming(sequence1, sequence2)

#!/usr/bin/env python
# Strings and Lists
def string_list(astring, alist):
    """The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice"""
    a,b,c,d=(alist)
    stringval1=astring[a:(b+1)]
    stringval2=astring[c:(d+1)]
    print(stringval1+" "+stringval2)

x='IwUrjMStreptopeliadgOL4UgeCV6troglodytestcCbrfKYhvLCzUhcntDPrWihjhKDiAelzxB1ItPPMwMAWo7EvJcpfFYgEYERcymkwb2k5MuWIhTi0UW08ie28GAPmgR4IS848ArjBMkm2mroMTQKBJN9AFMiNtzaTPWlwlVM71uzBwDx.'
y=[6,17,29,39]
string_list(x,y)

#!/usr/bin/env python
# Variables and some arithmetic
def variables_arithmetic(a, b):
    """The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths aa and bb."""
    c=(a**2+b**2)
    return c
print(variables_arithmetic(991, 821))

#!/usr/bin/env Python
#Conditions and loops
def cond_loop(a,b) :
    """Returns the sum of all odd integers from a through b, inclusively. """
    val = []
    while a < b :
        if a % 2 == 0 :
            val.append(a+1)
            a = a + 2
        else :
            a = a + 1
    #print(val)
    print(sum(val))

cond_loop(4603, 8843) # works for any even odd pairs of numbers

#!/usr/bin/env python
# Dictionaries
def dict_ss(textfile):
    """The number of occurrences of each word in textfile, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order."""
    words=textfile.split()
    wordfreq=[]
    for word in words :
        wordfreq.append(words.count(word))
    result = dict(zip(words, wordfreq))
    # Defining the result as list will make it difficult to manipulate, eg. to display pairs of key-values as effectively if defined as dictionary.
    for key, value in result.items():
        print(key+' '+str(value))

# Unlike in Python 2, the zip function in Python 3 returns an iterator. Iterators can only be exhausted (by something like making a list out of them) once.The purpose of this is to save memory by only generating the elements of the iterator as you need them, rather than putting it all into memory at once. If you want to reuse your zipped object, just create a list out of it.

dict_ss('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')

#!/usr/bin/env python
#Trancribing DNA to RNA 
def transcribe(DNA):
    """Returns the transcribed RNA string of t"""
    RNA = ''
    for x in DNA:
        if x != 'T':
            RNA += str(x)
        else:
            RNA += 'U'
    print(RNA)

transcribe('CTCTCACTAGGTTGTCTGTGTACGACTCCCCATTTATCCAACAATTTCCATTCATGGAACATCCGCGTCAACCCCGAGTCGTTATTGTGTTGACGTGCCCGTACAAACGACTAAGTGTCGCGTAAATTGTAACGGAAAGCCTTCGACGTCACTATTTGTTAACTTCAATGCGTAATCTAGGCGCTATTGCGGATGATTAATTATGTGCCATGGGCAAGAGTCCGCAGCGGCTTAGGCAGGTTGTATTTAGATCATAATGGCTAACATTATACAAGCAGCAAACGTCTAAGGTCACTAGTTGGAGTTGACTTCACCTACCGCTGACCCAGGGCATATTGAGCTCGGTTGGCAGGCGGTCAAGTCATGAGCGCCGAATATCTTCGCGTGCGTCCTACATTCGTAAGCAATTATCCTCCGTAATAGGGGCAGTTCTCTAAGGCCGATGGTACTAGTCTCACTTCATAATGGTCCTTGCGTTTTAGCTTCTCCCCACGCACAGCGACTAGCCACTAGATACACGGCGGCCCTGGTGTTAGCTCCCGGCGCTTACCAGGCAATCGGACATAGAGGCAGTCGTATTTAACGTAATCACGATGAAAGATTAACAGAGAGGCCCAGCAAAGTACGCTAACCTCCTGGTAGAATGATCTCGTTCCCTAGTGGTCTGCTGCGTTTAATACGGTATTGAGCTCTGTAGTTTCTAGAAGGGAGATCGCAATTTACATTCAGTAAAGTTACCAAACATGCGGGGGTGACAATAAACCGCGACTACTGTGCCCTTCCTCTATTTACGTATCGCTGCACCCCGCTATCAAATTAGTGGGCCTTGCCGCTGATGCAACTTGATAAGTACTCTGAATCATTTTACAGAGCAGAGGGCCTAAGCTCCTAGTCAGTGATGTTAGCCTCACTTGTTGGATCGCTTCCCGATTTGTCGAATATTTGGAAGAA')


