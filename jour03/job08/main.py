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
       if letter == word[0]:
           arrayWord.append(letter.lower())

# PARTIE HISTOGRAMME

plt.figure(figsize=(12, 5))
plt.hist(sorted(arrayWord), bins=26, density=True, color='orange', edgecolor='black', linewidth=1.4)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1))
plt.ylabel('Pourcentage (%)')
plt.suptitle('Pourcentage de présence de chaque lettre en début de mot.')

plt.show()
f.close()
