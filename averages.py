# Calculating Expected Offspring - E(X) = k * P(X=k)

import numpy as np
def expected_value(file):
    """
    Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of 
    couples in a population possessing each genotype pairing for a given factor. In order, the six given integers 
    represent the number of couples having the following genotypes:
    AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the 
    assumption that every couple has exactly two offspring. 
    """
    Pgen = np.array([1, 1, 1, 0.75, 0.5, 0]) # corresponding to Mendel Law
    with open(file) as f:
        d = f.read().replace('\n','').split(' ')
        d = [ x for x in d if x is not '']
        d = np.array([int(x) for x in d])
        dominant = Pgen * d

        return (np.sum(dominant)) * 2

print(expected_value('rosalind_iev.txt'))
