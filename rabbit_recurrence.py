#Fibonacci - Recurrence relationship - but the problem given is multi-nacci sequence of order k
memo = {0:0, 1:1}
def rabbit_fib(n,k):
    '''The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs '''
    if not n in memo:
        memo[n] = rabbit_fib((n-1),k) + k*rabbit_fib((n-2), k)
    return memo[n]

print(rabbit_fib(60,5))
