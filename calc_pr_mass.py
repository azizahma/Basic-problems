# Calculating Protein Mass

with open('mass_table') as f:
    d = [ x for x in f.read().strip().replace('\n',' ').split(' ') if x != '' ]
    d_key = d[0::2]
    d_val = d[1::2]
    d_val = [ float(x) for x in d_val ]
    dct = dict(list(zip(d_key, d_val)))

def pr_mass(file):
    with open(file) as f:
        m = sum(sum([v for k,v in dct.items() if k == x]) for x in f.read())
        print(m)

pr_mass('rosalind_prtm.txt')



