import pygame
import sys
from random import randint

SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE // 3
INF = float('inf')
vec2 = pygame.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class Board:
    def __init__(self, game):
        self.game = game
        self.field_image = self.getScaledImage(path='assets/field.png', res=(SCREEN_SIZE, SCREEN_SIZE))
        self.O_image = self.getScaledImage(path='assets/o.svg', res=[CELL_SIZE]*2)
        self.X_image = self.getScaledImage(path='assets/x.svg', res=[CELL_SIZE]*2)
        self.game_array = [[INF, INF, INF], [INF, INF, INF], [INF, INF, INF]]
        self.player = randint(0, 1)
        self.line_indices_array = [[(0,0), (0,1), (0,2)],  # horizontal
                                   [(1,0), (1,1), (1,2)],  # horizontal
                                   [(2,0), (2,1), (2,2)],  # horizontal
                                   [(0,0), (1,0), (2,0)],  # vertical
                                   [(0,1), (1,1), (2,1)],  # vertical
                                   [(0,2), (1,2), (2,2)],  # vertical
                                   [(0,0), (1,1), (2,2)],  # diagonal
                                   [(0,2), (1,1), (2,0)]]  # diagonal
        self.winner = None
        self.game_steps = 0
        self.font = pygame.font.SysFont('Verdana', CELL_SIZE // 5, True)
    
    def check_winner(self):
        for line_indices in self.line_indices_array:
           sum_line = sum([self.game_array[i][j] for i, j in line_indices])
           if sum_line in {0, 3}:
               self.winner = 'XO'[sum_line == 0]
               self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                   vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]
    
    def run_game_process(self):
        current_cell = vec2(pygame.mouse.get_pos()) // CELL_SIZE 
        col, row = map(int, current_cell)
        left_click = pygame.mouse.get_pressed()[0]
        
        if left_click and self.game_array[row][col] == INF and not self.winner:
            self.game_array[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()
        
    def draw_winner(self):
        if self.winner :
            pygame.draw.line(self.game.screen, "red", *self.winner_line, CELL_SIZE // 8)  
            label = self.font.render(f'Le joueur {self.winner} a gagné!', True, (239,213,144), "#29D2DD")
            self.game.screen.blit(label, (SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 4)) 
            
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x,y) * CELL_SIZE)
                
                # if obj == 0:
                #     self.game.screen.blit(self.O_image, (x*CELL_SIZE, y*CELL_SIZE))
                # elif obj == 1:
                #     self.game.screen.blit(self.X_image, (x*CELL_SIZE, y*CELL_SIZE))
            
            # for x, cell in enumerate(row):
            #     if cell == 0:
            #         self.game.screen.blit(self.O_image, (x*CELL_SIZE, y*CELL_SIZE))
            #     elif cell == 1:
            #         self.game.screen.blit(self.X_image, (x*CELL_SIZE, y*CELL_SIZE))
        
    def draw (self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()
        
    
    @staticmethod
    def getScaledImage(path, res):
        img = pygame.image.load(path)
        return pygame.transform.smoothscale(img, res)

    def print_caption(self):
        pygame.display.set_caption(f'Au tour du Joueur "{"OX"[self.player]}"!')
        if self.winner:
            pygame.display.set_caption(f'Le joueur "{self.winner}" a gagné! Appuyez sur espace pour rejouer.')
        elif self.game_steps == 9:
            pygame.display.set_caption(f'Partie nulle! Appuyez sur espace pour rejouer.')
            label = self.font.render(f'Match null ! appuyer sur espace pour recommencer', True, (239,213,144), "#29D2DD")
            self.game.screen.blit(label, (SCREEN_SIZE // 2 - label.get_width() // 2, SCREEN_SIZE // 4)) 
            
    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.clock = pygame.time.Clock()
        self.board = Board(self)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_game()
        
    def new_game(self):
        self.board = Board(self)
        
    def run(self):
        while True:
            self.board.run()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)
            # self.screen.fill((255, 255, 0))
            
if __name__ == '__main__':
    game = Game()
    game.run()
    
