#Translating of DNA string to Protein string - complexity when 'directly passing from DNA to protein:
#1 - Not all DNA will be transcribed into RNA (ie. junk DNAs)
#2 -Translation can begin at any position along a strand of DNA
#ORF starts with a 'start' codon and ends with a 'stop' codon without any other 'stop' codon in between
import re
with open('file') as dna:
    dna = ''.join(line.strip() for line in dna)
    seq = re.findall('[C,G,A,T]', dna)
    seq = ''.join(seq)
    #seqr = ''.join(reversed(seq)) ## bongok haper?? this is not the way to define 'reverse complement'
    seqr = []
    for s in seq:
        if s == 'A':
            s = 'T'
        elif s == 'G':
            s = 'C'
        elif s == 'T':
            s = 'A'
        elif s == 'C':
            s = 'G'
        else:
            s = s
        seqr.append(s)

seqr = ''.join(reversed(seqr))

#DNA codon table
dct = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': 'stop', 'TAG': 'stop', 'TGT': 'C', 'TGC': 'C', 'TGA': 'stop', 'TGG': 'W', 'CTT': 'L',
        'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
        'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
        'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N',
        'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V',
        'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D',
        'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
start = [k for (k, v) in dct.items() if v == 'M']
stop = [ k for (k,v) in dct.items() if v == 'stop']

def ORF(x):
    nuc = []
    for i in range(len(x)+1):
        codon = ''.join(x[i:i+3])
        if codon in start:
            for y in range(i,len(x)+1, 3):
                xy = x[i:y]
                last = xy[-3:]
                st = xy[:3]
                if last in stop:
                    codes = [ xy[i:i+3] for i in range(0,len(xy),3) ]
                    nuc.append(codes)
                    break
                if last in start and y != (i+3):
                    codes = [xy[i:i + 3] for i in range(0, len(xy), 3)]
                    codes = codes[:-1]
                    nuc.append(codes)
    pr = []
    for c in nuc:
        for cc in c:
            code = [v for (k, v) in dct.items() if k == cc]
            pr.append(code)
    pr = [item for sublist in pr for item in sublist]
    prjoin = ''.join(pr)
    prsplit = prjoin.split('stop')
    prsplit = [ x for x in prsplit if x is not '' ]
    return list(set(prsplit))

results = ORF(seq), ORF(seqr)
results = [ x for sublist in results for x in sublist ]
print('\n'.join(list(set(results))))