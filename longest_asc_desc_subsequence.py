# Longest Increasing Subsequence

with open('input') as f:
    d = f.readlines()
    d = [x.replace('\n', '') for x in d]
    n = int(d[0])
    p = d[1].split(' ')

def longest_subsequence(n,p):
    """
    Given: A positive integer n≤10000 followed by a permutation π of length n.
    Return: A longest increasing subsequence of ππ, followed by a longest decreasing subsequence of π.
    """
    print(n)
    print(p)
    


longest_subsequence(n,p)