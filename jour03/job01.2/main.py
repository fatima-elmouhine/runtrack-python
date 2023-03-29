import re
f = open('data.txt','r')
text = f.read()
res = len(re.findall(r'\w+', text))
print("Ce fichier contient : ",res," mots")
f.close()