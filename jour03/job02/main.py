import re
from os.path import dirname, abspath, join

f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
nbr = input('Entrez un nombre: ')
text = f.read()
arrayWord = []
res = len(re.findall(r'\w+', text))
for word in re.findall(r'\w+', text):
    if len(word)== int(nbr):
        arrayWord.append(word)
f.close()

print("Ce fichier contient : ",len(arrayWord)," mots")