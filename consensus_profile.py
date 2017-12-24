def consensus_profile(file):
    '''A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)'''
    import pandas as pd
    import re
    import csv
    with open(file) as f:
        fr = f.read()
        frjoin = ''.join(line.strip() for line in fr)
        frsplit = frjoin.split('>')
        cleanlist = [f for f in frsplit if f is not '']
        #print(cleanlist)

        idx = []
        jseq = []
        for seq in cleanlist:
            i = re.findall('^Rosalind_+\d', seq)
            j = re.findall('[C,G,A,T]*', seq)
            idx.append(i)
            jseq.append(j)

        listidx = [y for x in idx for y in x]
        listseq = [y for x in jseq for y in x]
        listseq2 = [x for x in listseq if x is not '']
        listinlistseq2 = [list(x) for x in listseq2]
        d = dict(list(zip(listidx,listinlistseq2)))
        #df = pd.DataFrame(d, index=['seq']) # to construct a DataFrame from a simple dict, either should have the items as lists, or else provide an index, or convert it a series
        df = pd.DataFrame(d)
        dft = df.transpose()
        profile = dft.apply(pd.value_counts).fillna(0) # to deal with strings of dict 'values'
        #print(profile)

        for col in profile:
            print(profile[col].idxmax(), end='')
        print('')
        valk = []
        for k,v in profile.iterrows():
            valk.append(k)
        #print(valk)
        profile.to_csv('val.csv', header=False, index=False)# a trick to remove column name, so able to present data as needed
        with open('val.csv','r') as val:
            reader = csv.reader(val)
            vallist = list(reader)
        #print(vallist)

        newlist = []
        for i in vallist:
            s = []
            for k in i:
                s.append(k[0])
            newlist.append(s)
        #print(newlist)

        dic = dict(list(zip(valk, newlist)))
        #print(dic)

        for k,v in dic.items():
            #print(v)
            print(k+': '+' '.join(v))

consensus_profile('file')