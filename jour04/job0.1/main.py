input_n = input("Entrez un nombre n: ");
x = 5

def calculExposant(n):
    if n == 0:
        return 1
    else:
        return x * calculExposant(n - 1)

print(calculExposant(int(input_n)))