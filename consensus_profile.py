# Finding a Most Likely Common Ancestor

def consensus_profile(file):
    with open(file) as f:
        d = ''.join(line.strip() for line in f.read()).split('>')
        d = [ x for x in d if x is not '' ]
        d1 = [x[:13] for x in d]
        d2 = [x[13:] for x in d]
        m = list(zip(*d2))
        #print(m)

        for i in range(len(m)):
            l = []
            for g in ['A', 'C', 'G', 'T']:
                l.append(m[i].count(g))
            makx = max(l)
            for g in ['A', 'C', 'G', 'T']:
                if makx == m[i].count(g):
                    print(g, end='')

        print()
        for g in ['A', 'C', 'G', 'T']:
            print(g, end=': ')
            for i in range(len(m)):
                print(m[i].count(g), end=' ')
            print()

consensus_profile('rosalind_cons.txt')
