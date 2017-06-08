#!/usr/bin/env Python
#Conditions and loops
def cond_loop(a,b) :
    """Returns the sum of all odd integers from a through b, inclusively. """
    val = []
    while a < b :
        if a % 2 == 0 :
            val.append(a+1)
            a = a + 2
        else :
            a = a + 1
    print(sum(val))

cond_loop(4603, 8843) # works for any even odd pairs of numbers
