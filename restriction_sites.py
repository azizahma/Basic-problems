#Locating 'restriction sites'
#eg. 'The billion years war' - bacteria VS virus
import re
def palindromic(file):
    '''The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.'''
    with open(file) as f:
        dna = ''.join(line.strip() for line in f)
        dna = re.findall('[C,G,A,T]', dna)
        dna = ''.join(dna)
        #print(dna)
        seq = []
        for x in range(4,13):
            seq_x = [ dna[a:a+x] for a in range(0,len(dna)) if len(dna[a:a+x]) == x ]
            seq.append(seq_x)
        #seq = [ item for sublist in seq for item in sublist ]
        for seqq in seq:
            #print(seqq)
            #Checking if each element is palindromic
            dna_dct = {'C':'G','A':'T','G':'C','T':'A'}
            for i,s in enumerate(seqq):
                #print(i+1,s)
                ss=[]
                for ele in s:
                    code = [ v for (k,v) in dna_dct.items() if ele == k ]
                    ss.append(code)
                ss = [ item for sublist in ss for item in sublist ]
                ss = ss[::-1] #to reverse arrangement of elements
                ss = ''.join(ss)
                if s == ss:
                    print(i+1, len(ss))
palindromic('file')