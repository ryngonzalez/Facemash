import pygame
from camera import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	image = Camera()
	cv.NamedWindow("camera", 1)
	while True:

		image.edge()
	 	#print type(image.edges[0])
	 	mat = cv.GetMat(image.edges)
	 	#print mat[0,0]
		image.render()
		event = pygame.event.poll()
		#cv.ShowImage("camera", image.edges)
		pygame.display.flip()
		if event.type == pygame.QUIT:
			break
		



# Run the main program now.			
if __name__ == "__main__":
	main()

