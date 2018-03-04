#Longest increasing subsequence - a simple measure of gene order similarity
#To search for the longest collection of genes that are formed in the same order in both chromosomes
#This doesn't work for small dataset eg. the sample dataset given - but who cares??
#There is something wrong with the process - the combination doesn't work complete.
def longest_subsequence(file):
    with open(file) as f:
        info = '>'.join(line.strip() for line in f)
        info = info.split('>')
        n = int(info[0])
        per = info[-1]
        per = per.split(' ')
        per = [ int(x) for x in per ]
        print(per)
        print(n)

        #for ascending order
        asc = []
        for i,p in enumerate(per):
            m = []
            if i == 0:
                m.append(per[i])
                next = min([ i for (i,x) in enumerate(per) if x > p ]) # the next position of element that meets this condition
                m.append(per[next])
                for j in range(next, len(per)):
                    if per[j] > m[-1]:
                        m.append(per[j])
            asc.append(m)

            if i >= 1:
                m.append(per[i])
                next = [ x for (i,x) in enumerate(per) if x > p ]
                next = next[i:]
                for nnext in next:
                    if nnext > m[-1]:
                        m.append(nnext)
            asc.append(m)
        #print(more)
        max_asc = max([ len(x) for x in asc ])
        res = [ x for x in asc if len(x) == max_asc ]
        print(' '.join(map(str,res[0])))

        # for descending order
        dsc = []
        for i, p in enumerate(per):
            l = []
            if i == 0:
                l.append(per[i])
                next = min([i for (i, x) in enumerate(per) if x < p])
                l.append(per[next])
                for j in range(next, len(per)):
                    if per[j] < l[-1]:
                        l.append(per[j])
            dsc.append(l)

            if i >= 1:
                l.append(per[i])
                next = [x for (i, x) in enumerate(per) if x < p]
                next = next[i:]
                for nnext in next:
                    if nnext < l[-1]:
                        l.append(nnext)
            dsc.append(l)
        # print(dsc)
        max_dsc = max([len(x) for x in dsc])
        resd = [x for x in dsc if len(x) == max_dsc]
        print(' '.join(map(str, resd[0])))

longest_subsequence('file.xx')