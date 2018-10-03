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


#print(read_data_fr_file('rosalind_long.txt'))
print(meanLength('rosalind_long.txt'))

#print(read_data_fr_file('input'))
#print(meanLength('input'))