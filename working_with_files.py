#Working with files

def working_with_files(file):
    """
    Given: A file containing at most 1000 lines.
    Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

    """

    with open(file) as f:
        lines = f.readlines() #[1:]
        print(''.join(lines[1:len(lines):2]))

working_with_files('rosalind_ini5.txt')