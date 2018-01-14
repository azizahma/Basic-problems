#The law of 'Independent Assortment' - Second Mendel's Law - 'alleles for different factors are inherited with no dependence on each other'
#Probability of getting AaBb offsprings from mates with AaBb is always 0.25 - regardless of the other mate's genotype - ie. each trial can only result in just 2 possible outcomes
#Following Binomial distribution: P(X=N) = (kCn/2**k)
#The problem however asks on probability of at least N AaBb in k generation (which is calculation for P(X=N), P(X=N+1), P(X=N+2),... P(X=# of the possible outcomes, in this case 2**k)
#Binomial generalisation of flipping coin H or T: p (exactly 2 scores in 6 attempts) = (6 2) 0.7**2 0.3**4
#Binomial generalisation for Mendel's Second Law: P(X=N) = (k N)(0.25**N) (0.75**(k-N))
#Probability = E(i=N,P) (P i)0.25**(i) 0.75**(P-i)


import math
def mendel_second(k,N):
    '''Return the probability that at least N AaBb will belong to the k generation of Tom's family tree'''
    P = 2**k
    prob = []
    for i in range(N, P+1):
        #print(i)
        #print(P)
        probability = ( math.factorial(P) / ( math.factorial(i) * math.factorial(P-i))) * (0.25**i) * (0.75**(P-i))
        prob.append(probability)
    return sum(prob)

print(mendel_second(5,8))