import pygame

#definition des dimensions de la table de jeu
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // ROWS

#définition des couleurs 

RED = (255,0,0)
WHITE = (255,255,255)
BLACK =(0,0,0)
BLUE = (0,0,255)
GREY = (128, 128,128)
LINE_COLOR = (0, 0, 0)
YELLOW = (245, 255, 196)
BROWN = (102,57,18)
BORColor=(56,31,10)

# on charge l'image qui s'affichera lorsque le pion atteind l'extrémité du damier

CROWN = pygame.transform.scale(pygame.image.load('./image/king.jpg'), (44,25))


pygame.init()


"""screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('DAME')
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]"""

