#Complementing a strand of DNA - a simpler solution

def reverse_complement(file):
    with open(file) as f:
        reverse = f.read().replace('\n','')[::-1]
        #print(str.maketrans('ACGT','TGCA')) # this is the character code used
        print(reverse.translate(str.maketrans('ATCG','TAGC')))

reverse_complement('rosalind_revc.txt')
