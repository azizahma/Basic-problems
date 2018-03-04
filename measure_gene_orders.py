#Longest increasing/decreasing subsequence - a simple measure of gene order similarity
#To search for the longest collection of genes that are formed in the same order in both chromosomes
import itertools
def longest_subsequence(file):
    with open(file) as f:
        info = '>'.join(line.strip() for line in f)
        info = info.split('>')
        n = int(info[0])
        per = info[-1]
        per = per.split(' ')
        per = [ int(x) for x in per ]
        #print(n, per) # I think there's a way in itertools that can work this out
        #print(n)
        print(per)
        c = []
        for i in range(n):
            comb = [ x for x in itertools.combinations(per, i) ] ##This is the problem with huge datasets, so I must get into another approach of doing this
            c.append(comb)
        c = [ item for sublist in c for item in sublist ]
        asc = [ item for item in c if item == tuple(sorted(item,reverse=False)) ]
        max_asc = max([ len(item) for item in asc ])
        res_asc = [ x for x in asc if len(x) == max_asc ]
        print(' '.join([ str(s) for s in res_asc[-1] ])) # as only one set is needed
        dsc = [ item for item in c if item == tuple(sorted(item,reverse=True)) ]
        max_dsc = max([ len(item) for item in dsc ])
        res_dsc =  [x for x in dsc if len(x) == max_dsc]
        print(' '.join([str(s) for s in res_dsc[-1]]))  # as only one set is needed, but it doesn't give what order appear first

longest_subsequence('file')