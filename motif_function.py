# Motif Implies Function

from urllib.request import urlretrieve
import re
def motif_implies_function(file):
    """
    Given: At most 15 UniProt Protein Database access IDs.
    Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list
    of locations in the protein string where the motif can be found.

    """
    with open(file) as f:
        d = f.read().replace('\n',' ').split(' ')
        d = [ x for x in d if x is not '']
        for x in d:
            link = 'http://www.uniprot.org/uniprot/'+x+'.fasta'
            urlretrieve(link,x+'.txt')
            with open(x+'.txt') as s:
                r = []
                seq = s.readlines()[1:]
                seq = ''.join([ x.replace('\n','') for x in seq ])
                motif = re.compile('N[^P][S|T][^P]')
                for i, j in enumerate(seq):
                    if j == 'N':
                        result = motif.match(seq[i:i+5])
                        if bool(result) is True:


                            r.append(i+1)
                if r: #if list not empty
                    print(x)
                    print(*r, sep=' ')

motif_implies_function('rosalind_mprt.txt')