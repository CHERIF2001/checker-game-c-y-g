from .constants import *

"""	Cette classe permet de gérer les pièces du damier """
class Piece:
	PADDING = 15
	OUTLINE = 2


	def __init__(self, row, col, color):
		self.row= row
		self.col =col
		self.color = color
		self.king= False
		self.x =0
		self.y =0
		self.calc_pos()
	#calculer les positions de x et y 
	def calc_pos(self):
		self.x = SQUARE_SIZE* self.col + SQUARE_SIZE//2
		self.y = SQUARE_SIZE* self.row + SQUARE_SIZE//2
    #cette méthode marque une piece comme un roi
	def make_king(self):
		self.king = True

    #Cette methode permet de dessiner une pièce
	def draw(self, win):
		radius = SQUARE_SIZE//2 - self.PADDING
		pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
		pygame.draw.circle(win, self.color, (self.x, self.y), radius)
		if self.king:
			win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

	# une methode qui permet le deplacement des pièces
	def move(self, row, col):
		self.row = row
		self.col = col 
		self.calc_pos()        # met à jour la position de la pièce


