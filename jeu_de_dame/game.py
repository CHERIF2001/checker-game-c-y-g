import pygame 
from .constants import * 
from .board import Board 


class Game: 
	def __init__(self, win):
		self._init()
		self.win = win


	def update(self):
		self.board.draw(self.win)
		self.draw_valid_moves(self.valid_moves)
		pygame.display.update()


	def _init(self):
		self.selected = None 
		self.board = Board()
		self.turn = RED 
		self