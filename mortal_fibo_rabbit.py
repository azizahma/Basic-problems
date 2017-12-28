def mortal_fib(n, m):
    '''The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.'''
    #Fn = F(n-1) + F(n-2) - F(n-(m+1))

    profile = [1,1]
    nos = 2
    while nos < n:
        if nos < m:
            profile.append(profile[-2] + profile[-1])
        elif nos == m:
            profile.append(profile[-2] + profile[-1] - 1)
        else:
            profile.append(profile[-2] + profile[-1] - profile[-(m+1)])

        nos += 1
    #print(profile)
    print(profile[-1])

mortal_fib(96,18)