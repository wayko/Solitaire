import pygame, sys
import random
from settings import *
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
GAMEBOARD = pygame.Surface((WIDTH,HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
WIN.fill(BOARD_COLOR)
class Board():
	def __init__(self):
		#Setup environment
		pygame.init()
		self.clock = pygame.time.Clock()
		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			self.clock.tick(FPS)

class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val
	def show(self):
		super().__init__()
		self.cards = [[self.val], [self.suit]]
		test = "{} of {}".format(self.val, self.suit)
		loadedCard = pygame.image.load(f'Cards/card{self.suit}{self.val}.png')
		WIN.blit(loadedCard,(0 * TILESIZE + loadedCard.get_width(),0 * TILESIZE + loadedCard.get_height()))	
		


class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
	
	def build(self):
		# row = GAMEBOARD.get_rect(topleft=(0,0))
		# print(row)
		for s in CARD_SUIT:
			for v in CARD_VAL:
				self.cards.append((Card(s,v)))
			
				
	def show(self):
		for c in self.cards:
			c.show()
	
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0,i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]	

	
	


deck = Deck()
deck.show()


if __name__ == '__main__':
	game = Board()
	game.run()