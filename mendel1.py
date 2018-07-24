__author__ = 'azizah'

#Mendel's First Law - simulation approach

with open('rosalind_iprb.txt') as f:
    inp = f.read().split(' ')
    k = int(inp[0])
    m = int(inp[1])
    n = int(inp[2])

import random
def mendel1(k, m, n):
    """
    Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
    k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    Return: The probability that two randomly selected mating organisms will produce an individual possessing
    a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
    """
    pop = k*['AA'] + m*['Aa'] + n*['aa']

    population = []
    for i in range(10000):
        pop2 = [random.choice(x) for x in random.sample(pop, 2)]
        pop2 = ''.join(pop2)
        population.append(pop2)

    print(1 - (population.count('aa')/10000))

mendel1(k,m,n)







