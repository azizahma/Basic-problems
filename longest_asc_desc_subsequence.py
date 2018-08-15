# Longest Increasing Subsequence

def longest_subsequence(file):
    """
    Given: A positive integer n≤10000n≤10000 followed by a permutation ππ of length n.
    Return: A longest increasing subsequence of ππ, followed by a longest decreasing subsequence of π.
    """
    with open(file) as f:
        d = f.readlines()
        d = [ x.replace('\n','') for x in d ]
        n = int(d[0])
        p =

longest_subsequence('input')