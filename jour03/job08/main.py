# import re
import matplotlib.pyplot as plt
import re
import matplotlib.ticker as mtick

# PARTIE MOTS
f = open('data.txt','r')
text = f.read()
arrayWord = []

for word in re.findall(r'[a-zA-Z]', text):
   for letter in word:
       if letter == word[0]:
           arrayWord.append(letter.lower())

# print(sorted(arrayWord))
# PARTIE HISTOGRAMME

plt.figure(figsize=(12, 5))
plt.hist(sorted(arrayWord), bins=18, color='orange', edgecolor='black', linewidth=1.4)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1000000))
plt.ylabel('Pourcentage (%)')
plt.suptitle('Pourcentage de présence de chaque lettre en début de mot.')

plt.show()
f.close()
