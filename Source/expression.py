import random
import config
import pygame
import os
from config import camera_resolution as res

class Expression:
	def __init__(self):
		self.expressions = config.expressions
		self.sides = ["left", "right"]
		self.score = 0
		self.threshold = config.threshold
	
	def choose(self):
		self.score = 0
		self.expression = random.choice(self.expressions)
		self.side = random.choice(self.sides)
		print self.side, self.expression
		wrong_expression = "Happy"

		while wrong_expression == self.expression:
			wrong_expression = random.choice(self.expressions)
		wrong_overlay 	= pygame.image.load(config.overlays[self.expression]).convert_alpha()
		correct_overlay = pygame.image.load(config.overlays[wrong_expression]).convert_alpha()
		if self.side == "left":
			self.wrong_overlay 	 = [wrong_overlay,pygame.Rect(40,res[1]/3,100,100)]
			self.correct_overlay = [correct_overlay,pygame.Rect(res[0]-240,res[1]/3,100,100)]
		else:
			self.wrong_overlay	 = [wrong_overlay, pygame.Rect(res[0]-240,res[1]/3,100,100)]
			self.correct_overlay = [correct_overlay,pygame.Rect(40,res[1]/3,100,100)]

	def increment(self, amount):
		self.score += amount
	def decrement(self, amount):
		self.score += amount * -1
