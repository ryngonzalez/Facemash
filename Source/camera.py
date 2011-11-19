#
#
#	Contains the functions and classes to control the camera.
#
#

import pygame
import numpy
import cv
from expression import *
import random
import kalman

class Camera:
	def __init__(self):
		self.capture = cv.CreateCameraCapture(0)
		self.loadCascades()
		self.numFaces = 0
		self.face_locations = []

	def optimize(self):
		image = cv.QueryFrame(self.capture)
		cv.Flip(image, None, 1)
		image_scale = 4
		# Set the image properties of the created images
		pixel_depth, channels = 8, 1
		# Create the images that are going to be drawn on
		gray = cv.CreateImage((image.width, image.height), pixel_depth, channels)
		small = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round(image.height / image_scale)),
								pixel_depth, channels)
		cv.CvtColor(image, gray, cv.CV_BGR2GRAY)
		cv.Resize(gray, small, cv.CV_INTER_LINEAR)
		cv.EqualizeHist(small, small)
		self.image_scale = image_scale
		self.small = small
		self.image = image
	
	def edges(self, image):
		gray = cv.CreateImage(cv.GetSize(image), 8, image.nChannels)
		cv.CvtColor(image, gray, cv.CV_BGR2GRAY)
		edges = cv.CreateImage(cv.GetSize(image), 8, image.nChannels)
		cv.Canny(gray,edges,60,60)
		
		return edges	
	
	def rectangle(self, image, d, thickness, color="white"):
		colors = { 	"white"	:(255,255,255),
					"black"	:(0,0,0),
					"red"	:(255,69,49),
					"green"	:(165,255,49),
					"blue"	:(41,89,214)   }
		cv.Rectangle(image, (d[0][0] * self.image_scale,d[0][1] * self.image_scale),
							(((d[0][0] + d[0][2]) * self.image_scale),
							( (d[0][1] + d[0][3]) * self.image_scale)), 
							  cv.RGB(colors[color][0], colors[color][1], colors[color][2]), thickness, cv.CV_AA, 0)

	def getRegion(self, image, x, y, width, height):
		final = cv.CreateImage( (int(width), int(height)), image.depth, image.nChannels)
		cv.GetRectSubPix(image, final, (x + width / 2, y +height / 2))
		return final
			
	def detect(self, cascade, min_size):
		haar_scale = 1.1
		min_neighbors = 2
		detected = cv.HaarDetectObjects(self.small, cascade, cv.CreateMemStorage(0), haar_scale,
										min_neighbors, 0, min_size)
		return detected

	def detectFace(self):
		self.faces = self.detect(self.faceCascade, (20,20))

	def detectEyes(self):
		self.left_eye 	= self.detect(self.right_eyeCascade,(18,12))
		self.right_eye 	= self.detect(self.left_eyeCascade, (18,12))
		
	def detectNose(self):
		self.nose = self.detect(self.nose_cascade,(25,15))
	
	def detectMouth(self):
		self.mouth = self.detect(self.mouth_cascade,(25,15))		 
		
	def loadCascades(self):
		self.faceCascade 		= cv.Load("Assets/Cascades/face.xml")
		self.right_eyeCascade 	= cv.Load("Assets/Cascades/right_eye.xml")
		self.left_eyeCascade 	= cv.Load("Assets/Cascades/left_eye.xml")
		self.mouth_cascade		= cv.Load("Assets/Cascades/mouth.xml")
		self.nose_cascade		= cv.Load("Assets/Cascades/nose.xml")
			

	def detectExpression(self, expression):
		self.optimize()		
		self.detectFace()
		image = self.image				
		if self.faces:
			for face in self.faces:
				self.rectangle(image, face, 1, "green")
				if self.side(face) == expression.side:
					if expression.score < expression.threshold:
						expression.increment()
						return False
					else:
						print "Correct!"
						return True
				else:
					return False


	def convert_to_pygame(self):
		image_rgb = cv.CreateMat(self.image.height, self.image.width, cv.CV_8UC3)
		cv.CvtColor(self.image, image_rgb, cv.CV_BGR2RGB)
		self.image = pygame.image.frombuffer(image_rgb.tostring(), cv.GetSize(image_rgb), "RGB")

	
	def side(self, face):
		x, y 	= 0, 0
		w, h 	= self.image.width, self.image.height
		left 	= pygame.Rect((x, y),((w / 2),h))
		right 	= pygame.Rect(((x + (1.5 * (w / 3))), y), ((w / 2),h))
		face 	= pygame.Rect((face[0][0] * self.image_scale, face[0][1] * self.image_scale),
							  (face[0][2] * self.image_scale, face[0][3] * self.image_scale))
		if left.contains(face):
			return "left"
		elif right.contains(face):
			return "right"
		else:
			return False
	

	def render(self, text=None, textpos=None):
		self.convert_to_pygame()
		if text and textpos:
			self.image.blit(text, textpos)
		pygame.display.get_surface().blit(self.image, (0,0))


