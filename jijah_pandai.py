# Text scramble program

def scramble(word):
    with open('code_table') as f:
        c = [ x for x in f.read().strip().replace('\n',' ').split(' ') if x != '' ]
        c_key = c[0::2]
        c_val = c[1::2]
        dct = dict(list(zip(c_key, c_val)))
        #print(dct)
        #print(word)
        t = [ [ v for k,v in dct.items() if k == x ]  for x in word ]
        t = [''.join(x) for x in t]
        return ''.join(t)

def unscramble(word):
    with open('code_table') as f:
        c = [ x for x in f.read().strip().replace('\n',' ').split(' ') if x != '' ]
        c_val = c[0::2]
        c_key = c[1::2]
        dct = dict(list(zip(c_key, c_val)))
        #print(dct)
        #print(word)
        t = [ [ v for k,v in dct.items() if k == x ]  for x in word ]
        t = [''.join(x) for x in t]
        return ''.join(t)


#with open('notes') as f: #########################TO SCRAMBLE
with open('scrambled_notes') as f: ######################TO UNSCRAMBLE
    fo = open('output.txt', 'w+')
    d = f.readlines()
    for x in d:
        xd = []
        for y in x.split():
            #xd.append(scramble(y)) #####################TO SCRAMBLE
            xd.append(unscramble(y)) ###########################TO UNSCRAMBLE
        output = ' '.join(xd)+'\n'
        fo.write(output)
    fo.close()


