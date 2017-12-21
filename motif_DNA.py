def motif_DNA(file):
    '''All locations of tt as a substring of ss.'''
    with open(file) as f:
        for idx,line in enumerate(iter(f)):
            if idx+1 == 1:
                s = line.strip() # removing white space at the same time
            else:
                t = line.strip() # removing white space at the same time
        #print(s)
        #print(t)
        #print(len(t))

        for i in range(0, len(s)+1):
            j = i + len(t)
            #print(s[i:j])
            if s[i:j] == t:
                #print(i+1)
                print(i+1, end=' ')

motif_DNA('file')