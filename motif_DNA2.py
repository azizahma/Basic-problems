__author__ = 'azizah'

# Finding a Motif in DNA

def motif_DNA():
    with open('rosalind_subs.txt') as f:
        inp = f.readlines()
        inp = [x.replace('\n','') for x in inp]
        seq = inp[0]
        m = inp[1]

        for i in range(len(seq)):
            motif = seq[i:i+len(m)]
            if motif == m:
                print(i+1, end=' ')

motif_DNA()