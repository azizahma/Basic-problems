#Finding a protein motif - from a list of uniport_id, obtain complete description and features of each (from UniProt site)
#For each protein possessing the N-glycosylation motif, output the access ID following a list of locations in the protein strings where the motif can be found
#For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

link = 'http://www.uniprot.org/uniprot/'
from urllib.request import urlretrieve #urllib & Requests libraries to automate file download in Python
import re
with open('file') as f:
    fjoin = ' '.join(line.strip() for line in f)
    fsplit = fjoin.split(' ') #fjoin & fsplit must be invoked to get the input filenames in a list without '\n'
    for protein in fsplit:
        url = link+protein+'.fasta'
        urlretrieve(url,protein+'.txt')
        #idx = []
        #jseq = []
        with open(protein+'.txt') as sequence:
            seq = sequence.readlines()[1:]
            seq = ''.join(line.strip() for line in seq)
            N_idx = []
            N = []
            for i,j in enumerate(seq):
                if j == 'N':
                    N.append(seq[i:i+4])
                    N_idx.append(i+1) #this is the N_location (or start sequence but not N-gly site)
            #to assert whether N_gly is really N-glycosylation site: validate values
            pattern = re.compile('N[^P][S|T][^P]')
            bN_gly = []
            for iN in N:
                result = pattern.match(iN)
                bN_gly.append(bool(result))
            #print(bN_gly)
            a= dict(list(zip(N_idx,bN_gly)))
            N_gly = []
            for k,v in a.items():
                if v == True:
                    N_gly.append(k)
            if N_gly != []:
                print(protein)
                print(*(sorted(N_gly, reverse=False)), sep=' ')

        #N{P}[ST]{P} - starts N, then any except P, then either S OR T, then any except P