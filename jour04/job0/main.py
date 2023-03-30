input_nbr = input("Entrez un nombre: ");

def factoriel(nbr):
    if nbr == 0:
        return 1
    else:
        return nbr * factoriel(nbr - 1)

print(factoriel(int(input_nbr)))
    