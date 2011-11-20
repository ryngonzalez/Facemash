import pygame
from config import *
from config import camera_resolution as res

class Text:
	def __init__(self, font, position, message, size, color):
		self.fonts = fonts
		self.positions = positions
		self.load(size,font)
		self.set_message(message, color)
		self.set_position(position)

	def load(self, size, font="lobster"):
		try:
			self.filename 	= pygame.font.match_font(self.fonts[font])
		except:
			self.filename 	= pygame.font.match_font(self.fonts["lobster"])
		self.font = pygame.font.Font(self.filename, size)

	def set_message(self, message, color):
		try:
			color = colors[color]
		except:
			color = color["white"]
		self.message = self.font.render(message,1,color)
	
	def set_position(self, position):
		try:
			p = self.positions[position]
		except:
			p = self.positions['middle_center']
		self.position = self.message.get_rect(centerx=p[0],centery=p[1])
	
	def change_font(self, font="lobster"):
		try:
			self.filename 	= pygame.font.match_font(self.fonts[font])
		except:
			self.filename 	= pygame.font.match_font(self.fonts["lobster"])
				

	def change_size(self, size):
		self.font = pygame.font.Font(self.filename, size)
	
