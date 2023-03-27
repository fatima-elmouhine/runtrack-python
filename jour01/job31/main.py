
input_word = input("Entrez un mot (sans accent ni majuscule ni espace): ")


def renderList(mot):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if not all(elmt in alphabet for elmt in mot):
        return "Le mot doit contenir uniquement des lettres minuscules de l'alphabet."

    lettres = list(mot)
    n = len(lettres)
    
    # Rechercher la première lettre qui est suivie d'une lettre plus petite dans l'ordre alphabétique.
    for i in range(n - 2, -1, -1):
        if lettres[i] < lettres[i+1]:
            # Trouver la lettre suivante la plus petite dans l'ordre alphabétique.
            j = i + 1
            while j < n and lettres[j] > lettres[i]:
                j += 1
            j -= 1
            # Échanger les deux lettres.
            lettres[i], lettres[j] = lettres[j], lettres[i]
            lettres[i+1:] = lettres[i+1:][::-1]
            
            return ''.join(lettres)
    
    return mot + " est déjà le plus grand mot possible."

print(renderList(input_word))
