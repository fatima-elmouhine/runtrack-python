
listNote = []

def renderList(list):
    for i in list:
        if (i < 40):
            listNote.append(i)
        else :
            if ((i + 2) % 5 == 0):
                listNote.append(i + 2)
            elif ((i + 1) % 5 == 0):
                listNote.append(i + 1)
            else:
                listNote.append(i)
    return listNote
renderList([50, 78, 83, 44, 39])
print(listNote)    