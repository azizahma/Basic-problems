#Variables and Some Arithmetic

def var_arith(file):
    with open(file) as f:
        x = f.read().split()
        a = int(x[0])
        b = int(x[1])
        y = a ** 2 + b ** 2
        return y

print(var_arith('rosalind_ini2.txt'))
