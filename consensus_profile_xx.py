# Finding a Most Likely Common Ancestor

# Using pandas

import pandas as pd
def consensus_profile(file):
    with open(file) as f:
        d = f.read().replace('\n','').replace('>',',').split(',')
        d = d[1:]
        d0= [ x[:13] for x in d ]
        d1= [ x[13:] for x in d ]

        d1 = [ [y for y in x] for x in d1 ]
        df = pd.DataFrame(dict(list(zip(d0,d1)))).transpose()
        profile = df.apply(pd.value_counts).fillna(0)

        #print(profile)
        for col in profile:
            print(profile[col].idxmax(), end='')
        print('')

        for m,n in profile.iterrows():
            ntolist = n.tolist()
            ntolist2 = [int(x) for x in ntolist]
            print(m+': '+' '.join(map(str, ntolist2)))

consensus_profile('rosalind_cons.txt')