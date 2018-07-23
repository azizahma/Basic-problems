__author__ = 'azizah'

def hamming_distance(file):
    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    """
    with open(file) as f:
        seq = f.readlines()
        seqc = []
        for y in seq:
            sc = [x for x in y.replace('\n','')]
            seqc.append(sc)
        compare_seqc = [ (seqc[0]==seqc[1]) for seqc[0],seqc[1] in zip(seqc[0],seqc[1]) ]
        score = compare_seqc.count(False)
        print(score)

hamming_distance('rosalind_hamm.txt')