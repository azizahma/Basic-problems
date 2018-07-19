#Dictionaries

def dicts(file):
    """
    Given: A string ss of length at most 10000 letters.
    Return: The number of occurrences of each word in ss, where words are separated by spaces. Words are case-sensitive, 
    and the lines in the output can be in any order.

    """
    out = open('out', 'w+')
    with open(file) as f:
        for line in f.readlines():
            word = line.split()

    key = []
    val = []
    for w in word:
        key.append(w)
        val.append(key.count(w))
    d = dict(zip(key,val))
    for k,v in d.items():
        print(k,v)
        print(k,v, file = out)

dicts('rosalind_ini6.txt')
