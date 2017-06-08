#!/usr/bin/env python
# Strings and Lists
def string_list(astring, alist):
    """The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice"""
    a,b,c,d=(alist)
    stringval1=astring[a:(b+1)]
    stringval2=astring[c:(d+1)]
    print(stringval1+" "+stringval2)

x='IwUrjMStreptopeliadgOL4UgeCV6troglodytestcCbrfKYhvLCzUhcntDPrWihjhKDiAelzxB1ItPPMwMAWo7EvJcpfFYgEYERcymkwb2k5MuWIhTi0UW08ie28GAPmgR4IS848ArjBMkm2mroMTQKBJN9AFMiNtzaTPWlwlVM71uzBwDx.'
y=[6,17,29,39]
string_list(x,y)
