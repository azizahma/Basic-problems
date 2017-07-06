#!/usr/bin/env python
# Working with files
def even_numbered_lines(filein,fileout):
    """Returns a file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines"""
    f = open(filein, 'r')
    fo= open(fileout, 'w+')
    file = f.readlines()
    result = (list(file)[1::2])
    fo.write("\n".join(result))

even_numbered_lines('test.txt','out.txt')
