#Finding a Shared Motif - longest common sub-sequence

def longest_common_sub(file):
    with open(file) as f:
        d = f.readlines()[1::2]
        d = [ x.replace('\n','') for x in d ]
        shortest_len = min([ len(x) for x in d ])
        shortest_seq = ''.join([ x for x in d if len(x) == shortest_len])
        other_seq = [ x for x in d if x != shortest_seq ]

        # what is the longest sub sequence that is common in all other sequences
        for x in other_seq:
            for i in range(len(x)):
                print(x[])


longest_common_sub('input')

