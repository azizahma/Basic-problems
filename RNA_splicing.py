#Genes are Discontiguous
#How does transcription achieved - DNA --mRNA -- aa: from DNA to aa
import re
def splice(file):
    '''A protein string resulting from transcribing and translating the exons of s.'''
    with open(file) as f:
        seqs = ''.join(line.strip() for line in f)
        seqs = seqs.split('>')
        seqs = [ x for x in seqs if x is not '' ]
    dna = []
    for s in seqs:
        ss = re.findall('[C,G,A,T]*', s)
        ss = [ x for x in ss if x is not '' ]
        dna.append(ss)
    dna1 = dna[:1]
    dna1 = [ item for sublist in dna1 for item in sublist ]
    dna1 = ''.join(str(b) for b in dna1)
    subs = dna[1:]
    #print(dna1)
    #print(subs)

    exons = []
    for introns in subs:
        i = ''.join(introns)
        l = len(''.join(introns))
        idna = [ dna1[x:l+x] for x in range(0, len(dna1)) if len(dna1[x:l+x]) == l ]
        loc = [ (j,l) for j,ii in enumerate(idna) if i == ii ]
    #splicing - cara bodo!!
        for j, l in loc:
            #print(j,l)
            dnaA = dna1[0:j]
            dnaB = dna1[j+l:len(dna1)]
            dna1 = dnaA+'>'*l+dnaB
            exons.append(dna1)
    exons = exons[-1]
    exons = exons.replace('>','')
    #translate exons
    protein = []
    dct = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
           'TAT': 'Y', 'TAC': 'Y', 'TAA': '', 'TAG': '', 'TGT': 'C', 'TGC': 'C', 'TGA': '', 'TGG': 'W',
           'CTT': 'L',
           'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
           'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
           'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N',
           'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V',
           'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D',
           'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    for m in range(0, len(exons),3):
        code3 = exons[m:m+3]
        aa = [ v for (k,v) in dct.items() if code3 == k ]
        protein.append(aa)
    protein = [ item for sublist in protein for item in sublist ]
    print(''.join(protein))

splice('file')


