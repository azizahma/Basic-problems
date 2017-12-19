def mendel_first(k,m,n):
    '''The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''
    total_pop = k+m+n
    #Probability of recessive phenotype - 1.aaxaa(1), 2.aaxAa(0.5), 3.Aaxaa(0.5), 4.AaxAa(0.25)
    Pr1 = (n/total_pop) * ((n-1)/(total_pop-1))
    Pr2 = (n/total_pop) * (m/(total_pop-1)) * 0.5
    Pr3 = (m/total_pop) * (n/(total_pop-1)) * 0.5
    Pr4 = (m/total_pop) * ((m-1)/(total_pop-1)) * 0.25

    #1 - Pr complement to probability of dominant trait
    print(1-(Pr1+ Pr2 + Pr3+ Pr4))

mendel_first(28,26,23)