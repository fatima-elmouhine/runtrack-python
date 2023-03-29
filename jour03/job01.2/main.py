import re
from os.path import dirname, abspath, join

f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
text = f.read()
res = len(re.findall(r'\w+', text))
print("Ce fichier contient : ",res," mots")
f.close()