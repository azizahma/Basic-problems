def consensus_profile2(file):
    '''A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)'''
    import re
    import pandas as pd

    with open(file) as f:
        fr = f.read()
        frjoin = ''.join(line.strip() for line in fr)
        frsplit = frjoin.split('>')
        cleanlist = [f for f in frsplit if f is not '']
        #print(cleanlist)

        idx = []
        jseq = []
        for seq in cleanlist:
            i = re.findall('^''Rosalind_+\d*', seq)
            j = re.findall('[C,G,A,T]*', seq)
            idx.append(i)
            jseq.append(j)
        #print(idx)
        #print(jseq)

    listidx = [y for x in idx for y in x]
    listseq = [y for x in jseq for y in x]
    listseq2 = [x for x in listseq if x is not '']
    listinlistseq2 = [list(x) for x in listseq2]
    d = dict(list(zip(listidx, listinlistseq2)))
    #print(d)

    df = pd.DataFrame(d)
    dft = df.transpose()
    profile = dft.apply(pd.value_counts).fillna(0)
    #print(profile)
    for col in profile:
        print(profile[col].idxmax(), end='')
    print('')
    #I think the problem with previous script (not acceptable) is the input feed 'prov.csv' in the middle of running the script - not supposed to be standard practise la kan...

    for m,n in profile.iterrows():
        nlis = n.tolist()
        nlis2 = [int(x) for x in nlis]
        print(m+': '+' '.join(map(str, nlis2)))

consensus_profile2('file')