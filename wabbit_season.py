#Mortal Fibonacci Rabbits

with open('rosalind_fibd.txt') as f:
    d = f.read().split(' ')
    n = int(d[0])
    m = int(d[1])

    #print(n,m)

def mortal_fibo(n,m):
    """
    Given: Positive integers n≤100 and m≤20.
    Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
    """
    f = [1] * n
    #print(f)
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
        if i >= m:
            f[i] = f[i] - f[(i-m)-1]
    print(f[-1])

mortal_fibo(n,m)

