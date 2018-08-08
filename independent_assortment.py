# Refer to Binomial Probability

import math
def xcy(x,y):
    f = math.factorial
    return f(x) / ( f(y) * f(x-y) )


def mendel_2(file):
    """
    Return: The probability that at least N AaBb organisms will belong to the k-th generation of Tom's family 
    tree (don't count the AaBb mates at each level). Assume that Mendel's second law holds for the factors. 
    """
    with open(file) as f:
        d = f.read().split(' ')
        k = int(d[0])
        N = int(d[1])
        P = 2 ** k # 2 offsprings from each organism in each generation
        probability = []
        for x in range(N,P+1): # x - for at least N organism of AaBb
            prob = xcy(P,x) * (0.25**(x)) * ((1 -0.25)**(P-x))   # use combinatorial P C x * (0.25**2) * ((1 -0.25) ** 2) - Mendel 2nd law: prob of getting AaBb
                                                                # from mating with AaBb (for all other genotypes) is always 0.25
            probability.append(prob)
        print(sum(probability))

mendel_2('rosalind_lia.txt')

