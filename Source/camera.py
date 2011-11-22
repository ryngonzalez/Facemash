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
import config

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
		colors = config.colors
		if len(d) == 2:
			cv.Rectangle(image, (d[0][0] * self.image_scale,d[0][1] * self.image_scale),
								(((d[0][0] + d[0][2]) * self.image_scale),
								( (d[0][1] + d[0][3]) * self.image_scale)), 
								  cv.RGB(colors[color][0], colors[color][1], colors[color][2]), thickness, cv.CV_AA, 0)
	  	else:
			cv.Rectangle(image, (d[0] * self.image_scale,d[1] * self.image_scale),
								(((d[0] + d[2]) * self.image_scale),
								( (d[1] + d[3]) * self.image_scale)), 
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
		self.faces = self.detect(self.face_Cascade, (20,20))

	def detectProfile(self):
		self.profiles = self.detect(self.profile_Cascade, (20,20))

	def detectEyes(self):
		self.left_eye 	= self.detect(self.right_eyeCascade,(18,12))
		self.right_eye 	= self.detect(self.left_eyeCascade, (18,12))
		
	def detectNose(self):
		self.nose = self.detect(self.nose_Cascade,(25,15))
	
	def detectMouth(self):
		self.mouth = self.detect(self.mouth_Cascade,(25,15))		 
		
	def loadCascades(self):
		self.face_Cascade 		= cv.Load("Assets/Cascades/face.xml")
		self.right_eyeCascade 	= cv.Load("Assets/Cascades/right_eye.xml")
		self.left_eyeCascade 	= cv.Load("Assets/Cascades/left_eye.xml")
		self.mouth_Cascade		= cv.Load("Assets/Cascades/mouth.xml")
		self.nose_Cascade		= cv.Load("Assets/Cascades/nose.xml")
		self.profile_Cascade	= cv.Load("Assets/Cascades/profile.xml")

	def locateFaces(self):
		self.optimize()		
		self.detectFace()
		self.detectProfile()
		if self.faces:
			for face in self.faces:
				self.face_locations.append((face[0][0], face[0][1], face[0][2], face[0][3]))
		elif self.profiles:
			for profile in self.profiles:
				self.face_locations.append((profile[0][0], profile[0][1], profile[0][2], profile[0][3]))

	def detectExpressions(self, expression):
		self.locateFaces()
		image 	= self.image
		f_l 	= self.face_locations
		total_x = 0
		total_y = 0
		total_w = 0
		total_h = 0
		x,y,w,h = 0,0,0,0
		if f_l:
			for f in f_l:
				total_x += f[0]
				total_y += f[1]
				total_w += f[2]
				total_h += f[3]
			
			x = total_x / len(f_l)
			y = total_y / len(f_l)
			w = total_w / len(f_l)
			h = total_h / len(f_l)
		m = [x,y,w,h]


		
		self.numFaces += 1
		if self.numFaces > 20:
			del self.face_locations[:]
			self.numFaces = 0

		if m:
			self.rectangle(image, m, 1, "red")
			if self.side(m) == expression.side:
				if expression.score < expression.threshold:
					expression.increment(1)
					return False
				else:
					# print "Correct!"
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
		if len(face) == 2:
			face 	= pygame.Rect((face[0][0] * self.image_scale, face[0][1] * self.image_scale),
								  (face[0][2] * self.image_scale, face[0][3] * self.image_scale))
	  	else:
			face 	= pygame.Rect((face[0] * self.image_scale, face[1] * self.image_scale),
								  (face[2] * self.image_scale, face[3] * self.image_scale))	  		
		if left.contains(face):
			return "left"
		elif right.contains(face):
			return "right"
		else:
			return False
	

	def render(self, text=None):
		self.convert_to_pygame()
		try:
			if text.message and text.position:
				self.image.blit(text.message, text.position)
		except:
			pass
		pygame.display.get_surface().blit(self.image, (0,0))


