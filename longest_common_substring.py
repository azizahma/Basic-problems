#Finding a Shared Motif - longest common sub-sequence

import re
def longest_common_sub(file):
    with open(file) as f:
        d = f.read().replace('\n','').split('>')
        d = ''.join([ x for x in d if x is not '' ])
        seq = re.findall('[C,G,A,T]*', d)
        seq = [ x for x in seq if x is not '']
        shortest_len = min([ len(x) for x in seq ])
        shortest_seq = ''.join([ x for x in seq if len(x) == shortest_len])
        other_seq = [ x for x in seq if x != shortest_seq ]

        # what is the longest sub sequence that is common in all other sequences
        for i in range(shortest_len,0,-1):
            for s in range(shortest_len-i+1):
                sub = shortest_seq[s:s+i]
                if all(sequence.find(sub) >= 0 for sequence in other_seq):
                    return sub

print(longest_common_sub('rosalind_lcsm.txt'))

