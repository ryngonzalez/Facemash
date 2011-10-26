import pygame, cv
capture = cv.CreateCameraCapture(0)
def showCamera(image):
	image_rgb = cv.CreateMat(image.height, image.width, cv.CV_8UC3)
	cv.CvtColor(image, image_rgb, cv.CV_BGR2RGB)
	image = pygame.image.frombuffer(image_rgb.tostring(), cv.GetSize(image_rgb), "RGB")
	return image
pygame.init()
screen = pygame.display.set_mode((640,480))
while True:
	image = cv.QueryFrame(capture)
	image = showCamera(image)
	screen.blit(image, (0,0))
	pygame.display.flip()
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
