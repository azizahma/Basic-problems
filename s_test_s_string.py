# http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_scs.pdf
# http://www.techiedelight.com/shortest-superstring-problem/
# https://www.geeksforgeeks.org/shortest-superstring-problem/

import re
import itertools

with open('input') as f:
    d = f.read().strip().replace('\n', '')
    dk = re.findall('Rosalind_[0-9]*', d)
    dv = re.findall('[A,C,G,T]*', d)
    dv = [x for x in dv if x is not '']
    dct = dict(list(zip(dk, dv)))
    length = int(sum([len(x) for x in dv]) / len(dk))

# left = dv[0]
# right = dv[2]
# print(left)
# print(right)
print(dct)

def overlap(left, right):
    '''Return: find the most overlapping string pair and combine the two, write it replacing the original sequences in the list'''
    results = []
    for i in range(length,0,-1):
        l = left[i:]
        r = right[:-i]
        if l == r: #and len(l) >= 5:
            results.append(len(l))
        else:
            results.append(0)
    return max(results)

def genome_assembly(dct):
    '''Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).'''
    o_lap = {}
    for lname in [k for k, v in dct.items()]:
        a = {lname: {}}
        zz = {}
        for rname in [k for k, v in dct.items() if k is not lname]:
            left = ''.join([v for k,v in dct.items() if k == lname])
            right = ''.join([v for k,v in dct.items() if k == rname])
            x = {rname: overlap(left, right)}
            zz.update(x)
        a[lname] = zz
        o_lap.update(a)
    #print(o_lap)
    #print(max([ [ j for i,j in v.items() ] for k,v in o_lap.items()]))
    ref = []
    for l,r in o_lap.items():
        ref.append(max([ v for k,v in r.items() ]))

    order = []
    for l in dk:
        ref2 = [ [i for i,j in v.items() if j==max(ref)] for k,v in o_lap.items() if k == l]
        ref2 = [''.join(x) for x in ref2]
        a = (l, ref2)
        a = (l, ''.join(a[1]))
        print(a)

        ## check seq-wise correct or not, then use dict? to follow

    #print(order)




        # ref2 = (l, [k for k,v in r.items() if v == max(ref)])
        # order.append(ref2)










#print(overlap(left,right))
genome_assembly(dct)
