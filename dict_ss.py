#!/usr/bin/env python
# Dictionaries
def dict_ss(textfile):
    """The number of occurrences of each word in textfile, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order."""
    words=textfile.split()
    wordfreq=[]
    for word in words :
        wordfreq.append(words.count(word))
    result = dict(zip(words, wordfreq))
    # Defining the result as a list will make it difficult to manipulate, eg. to display pairs of (Python dictionary) key-values as effectively if defined as dictionary.
    for key, value in result.items():
        print(key+' '+str(value))

# Unlike in Python 2, the zip function in Python 3 returns an iterator. Iterators can only be exhausted (by something like making a list out of them) once.The purpose of this is to save memory by only generating the elements of the iterator as we need them, rather than putting it all into memory at once. If you want to reuse your zipped objects, just create a list out of it.

dict_ss('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')
