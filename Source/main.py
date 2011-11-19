#
#
#	This is the start. Let's make something great.
#
#

import pygame, cv
from camera import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	image = Camera()
	expression = Expression()
	while True:
		expression.choose()
		is_correct = False
		lobster = pygame.font.match_font('lobster1.4')
		font = pygame.font.Font(lobster, 36)
		text = font.render(expression.expression + " on the " + expression.side, 1, (255,255,255))
		textpos = text.get_rect()
		textpos = text.get_rect(centerx=screen.get_width()/2)
		while not is_correct:
			is_correct = image.detectExpression(expression)
			#print expression.score
			image.render(text, textpos)
			pygame.display.flip()
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				break
		event = pygame.event.poll()
		pygame.display.flip()
		if event.type == pygame.QUIT:
			break


# Run the main program now.			
if __name__ == "__main__":
	main()

