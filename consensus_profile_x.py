# Finding a Most Likely Common Ancestor

def consensus_profile(file):
    with open(file) as f:
        d = f.read().replace('\n','').split('>')
        d = d[1:]
        d1 = [ x[13:] for x in d ]

        m = list(zip(*d1))
        profile = list(map(lambda x: dict((g, x.count(g)) for g in "ACGT"), m))
        cons = [max(x, key=x.get) for x in profile]
        print(''.join(cons))

        for x in 'ACGT':
            vv = []
            for y in profile:
                z = [ v for (k,v) in y.items() if k == x ]
                vv.append(z)
            v = [str(vv[i][0]) for i in range(len(vv))]
            print(x+': '+' '.join(v))

consensus_profile('rosalind_cons.txt')
