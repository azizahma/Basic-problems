# Longest Ascending and Descending Subsequence

with open('rosalind_lgis.txt') as f:
    d = f.readlines()
    d = [x.replace('\n', '') for x in d]
    n = int(d[0])
    p = d[1].split(' ')
    p = [ int(x) for x in p ]
    p_rev = reversed(p)

# via linear array
def longest_subsequence(n,p):
    """
    Given: A positive integer n≤10000 followed by a permutation p of length n.
    Return: A longest increasing subsequence of p, followed by a longest decreasing subsequence of p.
    """
    inc = [(0, [])] * (n+1)
    dec = [(0, [])] * (n+1)
    for i in p:
        x,y = max(inc[:i])
        m,n = max(dec[i:])
        inc[i] = (x+1,y+[i])
        dec[i] = (m+1,n+[i])

    print(*max(inc)[1])
    print(*max(dec)[1])

longest_subsequence(n,p)
