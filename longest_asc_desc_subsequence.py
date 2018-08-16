# Longest Increasing Subsequence

with open('rosalind_lgis.txt') as f:
    d = f.readlines()
    d = [x.replace('\n', '') for x in d]
    n = int(d[0])
    p = d[1].split(' ')
    p = [ int(x) for x in p ]
    p_rev = p[::-1]

# via linear array
def longest_subsequence(n,p):
    """
    Given: A positive integer n≤10000 followed by a permutation p of length n.
    Return: A longest increasing subsequence of p, followed by a longest decreasing subsequence of p.
    """
    ss_inc = [[]] * (n+1)
    for i in p:
        ss_inc[i] = max(ss_inc[:i], key = len) + [i]

    return ss_inc[i]

print(*longest_subsequence(n,p))
print(*longest_subsequence(n,p_rev)[::-1])