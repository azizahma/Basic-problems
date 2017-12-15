#Fibonacci - Recurrence relationship - but the problem given is multi-nacci sequence of order k
memo = {0:0, 1:1}
def rabbit_fib(n,k):
    if not n in memo:
        memo[n] = rabbit_fib((n-1),k) + k*rabbit_fib((n-2), k)
    return memo[n]

print(rabbit_fib(60,5))
