#Enumerating k-mers Lexicographically
#Basically, I just use itertools permutations and product, then drop any duplicate elements
import re
import itertools
def enumerate_k_mers(file):
    '''All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).'''
    with open(file) as f:
        info = ' '.join(line.strip() for line in f)
        alphabet = re.findall('[A-Z]',info)
        alphabet = sorted(alphabet)
        n = re.findall('\d*', info)
        n = [ x for x in n if x is not '' ]
        n = int(''.join(n))
        r = [ x for x in itertools.permutations(alphabet,n) ]
        r = [ ''.join(b) for b in r ]
        rr = [ x for x in itertools.product(alphabet, repeat=n) ]
        rr = [ ''.join(b) for b in rr ]
        results = r + rr
        results = sorted(list(set(results)))  # need to drop any duplicates as well!!
        print('\n'.join(results))

enumerate_k_mers('file')
