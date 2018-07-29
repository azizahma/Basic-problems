#Rabbits and Recurrence Relations (each term is generated from the previous value, with starting value - {0:1, 1:1}

with open('rosalind_fib.txt') as f:
    inp = f.read().replace('\n', '').split(' ')
    n = int(inp[0])
    k = int(inp[1])

    #print(n,k)

def fibo(n,k):
    """
    Given: Positive integers n≤40 and k≤5.

    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
    generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    """
    f = [1] * n
    for i in range(2, n):
        f[i] = f[i-1] + k* f[i-2]
    print(f[-1])

fibo(n,k)