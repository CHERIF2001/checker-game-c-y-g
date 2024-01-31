# on importe nos packages 

import pygame
from jeu_de_dame.constants import *
from jeu_de_dame.game import Game

# pour 60 images par secondes 

FPS= 60

# Pour lire le jeu 
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jeu de dame de Cherif, Gracia et Yann') # intitulé de notre jeu


# on definie une fonction qui gere les positions par rapport à la souris 
def get_row_col_from_mouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col


# pour gerer la logique du jeu (déplacement du jeu, gagnant perdant, click en association avec la classe Game)
def main():
	run = True 
	Clock = pygame.time.Clock()
	game = Game(WIN)


	while run:
		Clock.tick(FPS)

		if game.winner() != None:
			print(game.winner())
			run = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col =  get_row_col_from_mouse(pos)
				game.select(row, col)

		
		game.update()

	pygame.quit()


main()