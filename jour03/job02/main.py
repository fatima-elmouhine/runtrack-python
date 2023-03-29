import re
f = open('data.txt','r')
nbr = input('Entrez un nombre: ')
text = f.read()
arrayWord = []
res = len(re.findall(r'\w+', text))
for word in re.findall(r'\w+', text):
    if len(word)== int(nbr):
        arrayWord.append(word)
f.close()

print("Ce fichier contient : ",len(arrayWord)," mots")