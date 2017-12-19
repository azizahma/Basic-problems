from decimal import *
import numpy as np

def GC_content(file):
    '''The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below'''
    getcontext().prec = 28
    with open(file) as f:
        fr = f.read()
        fr1 = ''.join([line.strip() for line in fr])
        fr2 = fr1.split('>')
        fr3 = [f for f in fr2 if f is not '']
        #Split list into dict, then do operation for information needed in there
        idx = []
        #val = []
        GC = []

        for n in range(len(fr3)):
            seq = fr3[n]
            i = seq[:13]
            v = seq[14:]
            vG = v.count('G')
            vC = v.count('C')
            vAll = len(v)
            GCp = Decimal(((vG+vC)/vAll)*100) #Binary arithmetic is a bit tricky for calculation of percentage, so the use of Decimal here.
            idx.append(i)
            #val.append(v)
            GC.append(GCp)


        d = dict(list(zip(idx, GC)))

        #Return sequence with max GC content within (a default) absolute error 0.001
        dmax = max(d.values())
        dmax_key = [k for k,v in d.items() if v == dmax]
        print(''.join(dmax_key))
        print(dmax)
        print(np.abs(dmax))

GC_content('filex.fa')