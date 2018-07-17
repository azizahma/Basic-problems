# Conditions and Loops

def conditions_loops(file):
    """
    Given: Two positive integers a and b (a<b<10000a<b<10000).
    Return: The sum of all odd integers from a through b, inclusively.

    """

    with open(file) as f:
        x = f.read().split()
        a = int(x[0])
        b = int(x[1])
        if a % 2 == 0:
            aa = a + 1
        else:
            aa = a
        if b % 2 == 0:
            bb = b - 1
        else:
            bb = b
        # print(aa,bb)

        print(sum(list(range(aa, bb + 1, 2))))


conditions_loops('rosalind_ini4.txt')