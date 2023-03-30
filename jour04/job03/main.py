input_n = input("Entrez un nombre n: ");
import random

arrayBoard = []
arrayBoard2 = []     
def inList(l, target):
    if l == []:
        return False
    elif l[0] == target:
        return True
    else:
        return inList(l[1:], target)

def drawChessBoard(n):
    if n == 0:
        return 1
    else:
        # print( " 0 " * int(input_n))
        arrayBoard.append(("0") * int(input_n))
        list(arrayBoard)
        return n * drawChessBoard(n - 1)

def markXinBoard(n):
    arrayIndex = []
    if n == 0:
        return 1
    else:
        arrayBoard2 = list(arrayBoard[random.randrange(0, int(n))])
        if "X" not in arrayBoard2[random.randrange(0, int(n))] : 
            arrayBoard2[random.randrange(0, int(n))] = "X"
    
        print(arrayBoard2)

        # print(inList(arrayIndex, "X"))
        
        # print(arrayBoard2)
        # print(arrayBoard2[0])
        # print(arrayBoard2[1])
        
        # arrayBoard[random.randint(0, int(n))] = "X"
        return n * markXinBoard(n - 1)
    
def printBoard(n):
    arrayBoard2 = list(arrayBoard[random.randrange(0, int(n))])
    print(arrayBoard2)

      
drawChessBoard(int(input_n))
# print( "-----------" * int(input_n))
markXinBoard(int(input_n))
print( "c est pas aligné correctement" )
# printBoard(int(input_n))