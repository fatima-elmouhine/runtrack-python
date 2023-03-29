import xml.etree.ElementTree as ET
import re
ext = []
tree = ET.parse('domains.xml')
root = tree.getroot()
def searchDomainInString(string):
    regex = re.compile(r'([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}')
    if regex.search(string):
        ext.append(regex.search(string).group())
        return True
    
    
for child in root:
    searchDomainInString(child.tag)
    for subchild in child:
        for child in subchild:
            searchDomainInString(child.text)
                
    
print("Nombre de domaine (sans le celui commenter à la ligne 5) : ",len(ext))
    
