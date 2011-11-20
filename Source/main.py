#
#
#	This is the start. Let's make something great.
#
#

import pygame 
import cv
import text
from camera import *
import event

def play():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	image = Camera()
	expression = Expression()
	state = 1
	score 	= 0
	while state !=0 :
		expression.choose()
		is_correct = False
		message = expression.expression
		message = text.Text("lobster", "top_center", message, 36, "white")
		score_text 	= text.Text("din_bold", "bottom_center", str(score)+" EXPRESSIONS", 36, "white")
		while not is_correct and state !=0:
			is_correct = image.detectExpressions(expression)
			#print expression.score
			image.render(message)
			screen.blit(expression.correct_overlay[0], expression.correct_overlay[1])
			screen.blit(expression.wrong_overlay[0], expression.wrong_overlay[1])
			screen.blit(score_text.message, score_text.position)
			pygame.display.flip()
			state = event.check()
		score += 1
		pygame.display.flip()

# def learn():


# Run the main program now.			
if __name__ == "__main__":
	play()

