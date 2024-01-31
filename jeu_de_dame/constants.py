import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//ROWS

#définition des couleurs 

RED = (255,0,0)
WHITE = (255,255,255)
BLACK =(0,0,0)
BLUE = (0,0,255)
GREY = (128, 128,128)

CROWN= pygame.transform.scale(pygame.image.load('./image/king.jpg'), (44,25))

#definition des dimensions de la table de jeu
pygame.init()
BOARD_SIZE = 8
TILE_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * TILE_SIZE
COLUMN = 8
ROW = 8
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('DAME')
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#Definition de couleur
LINE_COLOR = (0, 0, 0)
YELLOW = (245, 255, 196)
BRUN = (102,57,18)
BORColor=(56,31,10)
