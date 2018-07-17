#Strings and Lists

def strings_lists(file):
    """
    Given a string (s) and indices a,b,c,d, returns the slice of this string from indices a through b and c through d 
    (with space in between), inclusively. 
    In other words, we should include elements s[b] and s[d] in our slice. 
    """
    with open(file) as f:
        ele = f.read().split()

        n = len(ele)
        #print(n)

        s = ele[0]
        a = int(ele[1])
        b = int(ele[2])
        c = int(ele[3])
        d = int(ele[-1])

        # print(s)
        # print(a)
        # print(b)
        # print(c)
        # print(d)

        print(s[a:b+1] + ' ' + s[c:d+1])

strings_lists('rosalind_ini3.txt')