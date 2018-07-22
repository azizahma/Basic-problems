#Rabbits and Recurrence Relations (each term is generated from the previous value, with starting value - {0:1, 1:1}

with open('rosalind_fib.txt') as f:
    inp = f.read().replace('\n', '').split(' ')
    n = int(inp[0])
    k = int(inp[1])


memo = {0:1, 1:1}
def recurrence_relation(x,y):
    """
    Given: Positive integers n≤40n and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
    generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    
    """
    if x not in memo:
        memo[x] = recurrence_relation((x-1), y) + k*recurrence_relation((x-2),y) # Fn = F(n-1)+F(n-2)
    return memo[x]

print(recurrence_relation(n,k))