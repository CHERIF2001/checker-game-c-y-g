import pygame
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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (245, 255, 196)
BRUN = (102,57,18)
BORColor=(56,31,10)


def draw_board():
    screen.fill(WHITE)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            color = YELLOW if (i + j) % 2 == 0 else BRUN
            pygame.draw.rect(screen, color, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.draw.line(screen, LINE_COLOR, (i * TILE_SIZE, 0), (i * TILE_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, LINE_COLOR, (0, i * TILE_SIZE), (WINDOW_SIZE, i * TILE_SIZE), 1)

    #bordure
    pygame.draw.line(screen, YELLOW, (0, 0), (0, WINDOW_SIZE), 20)
    pygame.draw.line(screen, YELLOW, (WINDOW_SIZE - 1, 0), (WINDOW_SIZE - 1, WINDOW_SIZE), 20)
    pygame.draw.line(screen, YELLOW, (0, WINDOW_SIZE - 1), (WINDOW_SIZE, WINDOW_SIZE - 1), 20)


    pygame.display.flip()

