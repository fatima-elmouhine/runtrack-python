# import re
import matplotlib.pyplot as plt
import re
import matplotlib.ticker as mtick
from os.path import dirname, abspath, join

# PARTIE MOTS
f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
text = f.read()
arrayWord = []

for word in re.findall(r'[a-zA-Z]', text):
    for letter in word:
        arrayWord.append(letter.lower())


# PARTIE HISTOGRAMME


plt.figure(figsize=(12, 5))
plt.hist(sorted(arrayWord), bins=26, color='orange', edgecolor='black', linewidth=1.4)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1000000))
plt.ylabel('Pourcentage (%)')
plt.suptitle('Pourcentage d\'apparition de chaque lettre')

plt.show()
f.close()

# print("Ce fichier contient : ",len(arrayWord)," mots")