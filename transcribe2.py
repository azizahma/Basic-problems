#Transcribing RNA into DNA

def transcribe(file):
    """
    Given: A DNA string tt having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    """
    with open(file) as f:
        dna = f.read()
        rna = dna.replace('T','U')
        print(rna)

transcribe('rosalind_rna.txt')
