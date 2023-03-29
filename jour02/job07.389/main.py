class Board:
    def __init__(self, i, j):
        self.board = [['O' for _ in range(j)] for _ in range(i)]
        self.rows = i
        self.columns = j
    
    def play(self, colNum, color):
        row = len(self.board) - 1
        while row >= 0 and self.board[row][colNum] != 'O':
            row -= 1
        if row >= 0:
            self.board[row][colNum] = color
        # if self.checkIfWin(color):
        #     print(color + " a gagné!")
        #     return True
    
    def print(self):
        for row in self.board:
            print(row)
    
    # def checkIfWin(self, color):
    #      for row in range(self.rows):
    #         for col in range(self.columns - 3):
    #             if self.board[row][col] == color and self.board[row+1][col] == color and self.board[row+2][col] == color and self.board[row+3][col] == color:
    #                 print(color + " a gagné!")
    #                 return True
    #             else:
    #                 return False
    
    def checkIfWin(self, color):
        # horizontal
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == color and self.board[row][col+1] == color and self.board[row][col+2] == color and self.board[row][col+3] == color:
                    return True
        
        # vertical
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == color and self.board[row+1][col] == color and self.board[row+2][col] == color and self.board[row+3][col] == color:
                    return True
        
        # diagonal (gauche to droite)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == color and self.board[row+1][col+1] == color and self.board[row+2][col+2] == color and self.board[row+3][col+3] == color:
                    return True
        
        # diagonal (droite - gauche)
        for row in range(self.rows - 3):
            for col in range(3, self.columns):
                if self.board[row][col] == color and self.board[row+1][col-1] == color and self.board[row+2][col-2] == color and self.board[row+3][col-3] == color:
                    return True
        
        return False


board = Board(6, 7)
game_over = False
current_player = 'J'
# while board.checkIfWin('J') != True or board.checkIfWin('R') != True:
# board.play(4, 'J')
# board.play(4, 'R')
# board.play(3, 'J')
# board.play(4, 'R')
# board.play(5, 'J')
# board.play(4, 'R')
# board.play(2, 'J')
# board.play(4, 'R')
while not game_over:
    colNum = int(input(current_player + ", choisissez une colonne : ")) # Get the column from the current player
    board.play(colNum, current_player)
    board.print()
    
    if board.checkIfWin(current_player): # Check if the current player has won
        print(current_player + " a gagné!")
        game_over = True
    else:
        current_player = 'R' if current_player == 'J' else 'J' # Switch to the other player's turn



