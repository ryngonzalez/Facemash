import random


class Expression:
	def __init__(self):
		self.expressions = ["Happy", "Sad", "Surprised", "Content", "Angry"]
		self.sides = ["left", "right"]
		self.score = 0
		self.threshold = 20
	
	def choose(self):
		self.score = 0
		self.expression = random.choice(self.expressions)
		self.side = random.choice(self.sides)
		print self.side, self.expression

	def increment(self):
		self.score += 1
