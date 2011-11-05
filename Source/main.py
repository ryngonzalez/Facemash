#
#
#	This is the start. Let's make something great.
#
#

import pygame, cv
from camera import *
# import settings
# import play
# import learn

class Game():

	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode(pygame.FULLSCREEN)
		pygame.display.set_caption('Facemash')
	def event(self, event):
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	image = Camera()
	while True:
		image.optimize()
		image.loadCascades()
		image.detectFace()
		faces = image.faces
		if faces:
			for ((x, y, w, h), n) in faces:
				pt1 = (int(x * image.image_scale), int(y * image.image_scale))
				pt2 = (int((x + w) * image.image_scale), int((y + h) * image.image_scale))
				h = h * image.image_scale
				w = w * image.image_scale
				cv.Rectangle(image.image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
		image.convert_to_pygame()
		screen.blit(image.image, (0,0))
		pygame.display.flip()
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break

# Run the main program now.			
if __name__ == "__main__":
	main()

