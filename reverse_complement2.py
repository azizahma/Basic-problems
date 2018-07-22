#Complementing a strand of DNA - a simpler solution

def reverse_complement(file):
    with open(file) as f:
        reverse = f.read().replace('\n','')[::-1]
        print(reverse.replace('A','a').replace('G','g').replace('T','A').replace('C','G').replace('a','T').replace('g','C'))

reverse_complement('rosalind_revc.txt')
