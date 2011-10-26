#
#
#	This is the start. Let's make something great.
#
#

import pygame, cv
# import settings
# import play
# import learn

class Game():

	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode(pygame.FULLSCREEN)
		pygame.display.set_caption('Facemash')
	def event(self, event):
		if event.type == QUIT:
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()

def main():
	game = Game()
	clock = pygame.time.Clock()
	running = True
	while running:
		clock.tick(60)
		pygame.display.flip()
		for event in pygame.event.get():
			game.event(event)

# Run the main program now.			
main()

