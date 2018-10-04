# Genome Assembly as Shortest Superstring

import re
def read_data_fr_file(file):
    with open(file) as f:
        d = f.read().strip().replace('\n','')
        dk = re.findall('Rosalind_[0-9]*', d)
        dv = re.findall('[A,C,G,T]*', d)
        dv = [ x for x in dv if x is not '' ]
        dct = dict(list(zip(dk,dv)))
        return dct

def meanLength(file):
    d = read_data_fr_file(file)
    length = sum([ len(v) for k,v in d.items()])/len(d)
    return length

# d = read_data_fr_file('rosalind_long.txt')
# #d = read_data_fr_file('input')
# left = [v for k, v in d.items()][0]
# right = [v for k, v in d.items()][1]

def getOlap(left, right):
    results = []
    for i in range(len(left)-1, 0, -1): # only need to iterate the len(left), as n the input data none of the reads are completely nested in another read
        l = left[i:]
        r = right[:-i]
        if l == r:  # and len(l) >= 5:
            results.append(len(l))
        else:
            results.append(0)
    return max(results)

def getAllOlap(d):
    o_lap = {}
    for lname in [k for k, v in d.items()]:
        a = {lname: {}}
        zz = {}
        for rname in [k for k, v in d.items() if k is not lname]:
            left = ''.join([v for k, v in d.items() if k == lname])
            right = ''.join([v for k, v in d.items() if k == rname])
            b = {rname: getOlap(left, right)}
            zz.update(b)
        a[lname] = zz
        o_lap.update(a)
    return o_lap

import pandas as pd
def prettyPrint(dd):
    df = pd.DataFrame(o_lap)
    df = df.fillna('-')
    return df

#We decide that true overlaps are the ones with an overlap larger than two (>2).
def findFirstread(dd):
    a = [[j for i,j in v.items() if j>2] for k,v in dd.items()]
    a = [ x for x in a if x != []]
    return a
    #a = [''.join(map(str,x)) for x in a]

    # a = max([ int(x) for x in a ])
    #
    # for k,v in dd.items():
    #     for i,j in v.items():
    #         if j == a:
    #             print(k)







#print(meanLength('rosalind_long.txt'))
#print(getOlap(left,right))
#o_lap = getAllOlap(read_data_fr_file('rosalind_long.txt'))
o_lap = getAllOlap(read_data_fr_file('input'))
#print(o_lap)
# for k,v in o_lap.items():
#     for i,j in v.items():
#         if j > 200: # meanLength('rosalind_long.txt')/2:
#             print(k, i, j)
print(prettyPrint(o_lap))
print(findFirstread(o_lap))


#print(read_data_fr_file('input'))
#print(meanLength('input'))