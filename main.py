# on importe les packages

import pygame 


FPS = 60 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


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
				pass


		game.update()

	pygame.quit()


main()