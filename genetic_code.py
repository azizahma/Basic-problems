def RNA_into_protein(f):
    rna = []
    dct = {'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'','UAG':'','UGU':'C','UGC':'C','UGA':'','UGG':'W','CUU':'L','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
    with open(f) as s:
        sr = s.read()
        for i in range(3, len(sr) + 1, 3): # which uses step=3 value for range() to iterate by 3s
            rna.append(sr[i-3:i])
        #print(rna)
        aa = [dct[k]for k in rna]
    #print(''.join(rna))
    print(''.join(aa))

RNA_into_protein('file')