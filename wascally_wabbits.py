#Rabbits and Recurrence Relations (each term is generated from the previous value, with starting value - {0:1, 1:1}

with open('rosalind_fib.txt') as f:
    inp = f.read().replace('\n', '').split(' ')
    n = int(inp[0])
    k = int(inp[1])

    print(n,k)

def fibo(n,k):

    p2, p1 = 1, 1
    for x in range(2,n):
        p2, p1 = p1,  k*p2 + p1

    return p1

print(fibo(n,k))

