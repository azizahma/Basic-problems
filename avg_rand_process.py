#To average a random process - E(x) = k * Pr(x=k)
#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

gen = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']

def convert_data(file):
    with open(file) as f:
        fr = f.read()
        fr = fr.split(' ')
        fr_l = []
        for i in fr:
            fr_l.append(i)
        fr_ll = [int(x) for x in fr_l if x is not ' ']
    #print(fr_ll)
    punnet_sq = [1, 1, 1, 0.75, 0.5, 0]

    w = []
    for i,j in enumerate(fr_ll):
        for k,v in enumerate(punnet_sq):
            if i == k:
                #print(j,v)
                w.append(j*v)

    return(sum(w)*2)

print(convert_data('file'))


#Combine two dictionary and appending values for common keys - is not a 'regular' (more pythonic) solution for problems.

#I was stuck at combining two dicts - I thought this is more 'pythonic' as dicts can be turned into a DataFrame - things get easy to manipulate...
