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
	score = 0
	sticker_image = pygame.image.load(config.stickers[config.sticker]).convert_alpha()
	while state !=0 :
		expression.choose()
		is_correct = False
		message = expression.expression
		message 	= text.Text("lobster", "top_center", message, 36, config.color)
		if score == 1:
			score_text 	= text.Text("lobster", "bottom_center", str(score) + " " + config.sticker, 36, config.color)
		else:
			score_text 	= text.Text("lobster", "bottom_center", str(score) + " " + config.sticker+"s", 36, config.color)
		correct 	= text.Text("lobster", "bottom_left", "Correct!", 24, config.color)
		time 		= pygame.time.Clock()
		t = config.time
		while not is_correct and state !=0 and (t/1000) > 0:
			t -= time.tick()
			ticker 	= text.Text("lobster", "bottom_left", str((float(round(t)/1000))), 36, config.color)
			is_correct = image.detectExpressions(expression)
			image.render(message)
			screen.blit(expression.correct_overlay[0], expression.correct_overlay[1])
			screen.blit(expression.wrong_overlay[0], expression.wrong_overlay[1])
			screen.blit(score_text.message, score_text.position)
			screen.blit(ticker.message, (ticker.position[0],ticker.position[1]))
			screen.blit(sticker_image, (config.positions['bottom_right'][0]-40,config.positions['bottom_right'][1]-30))
			pygame.display.flip()
			state = event.check()
		if t/1000 > 0 and state !=0:
			score += 1
			in_the_middle = False
			while not in_the_middle:
				image.optimize()
				image.detectFace()
				move_back = text.Text("lobster", "middle_center", "Move back to the center!", 64, config.color)
				for face in image.faces:
					side = image.side(face)
					image.render()
					screen.blit(move_back.message, move_back.position)
					pygame.display.update()
					if side != expression.side:
						in_the_middle = True
		pygame.display.update()

def learn():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	state = 1
	alpha = 255
	screen_rect = pygame.Surface((640,480))	
	color = pygame.Color(0,0,255)
	screen_rect.fill(color)
	sticker_images = []
	smile = pygame.image.load(config.overlays['Happy']).convert_alpha()
	play_button = pygame.image.load("Assets/Buttons/play.png").convert_alpha()
	for c in config.stickers:
		sticker_images.append(pygame.image.load(config.stickers[c]).convert_alpha())
	for s in sticker_images:
		s.set_alpha(0)
	correct = text.Text("lobster", "middle_center", "Good Job!", 48, "white") 
	welcome = text.Text("lobster", "middle_center", "Welcome!", 48, "white")
	fun_text = ["Today we're", "going to have", "some fun making faces!"]
	show_text = ["Using your face, show me how you're feeling:"]
	reward_text = ["I'm glad to see you! Thanks for sharing with me.", "Choose a sticker you like by clicking it:"]
	happy_text = ["This is what happy looks like.","Can you show me a happy face?"]
	l_side_text = ["<- This is the left", "Can you move to the left side?"]
	r_side_text = ["This is the right ->", "Can you move to the right side?"]
	h_side_text = ["Happy"]
	final_text = ["Congratulations!","You're now ready to play."]
	f_text = []
	s_text = []
	r_text = []
	h_text = []
	ls_text = []
	rs_text = []
	hs_text = []
	fin_text = []
	for t in fun_text:
		f_text.append(text.Text("lobster", "middle_center", str(t), 36, "white"))
	for t in show_text:
		s_text.append(text.Text("lobster", "top_center", str(t), 28, "white"))
	for t in reward_text:
		r_text.append(text.Text("lobster", "top_center", str(t), 28, "white"))
	for t in happy_text:
		h_text.append(text.Text("lobster", "top_center", str(t), 28, "white"))
	for t in l_side_text:
		ls_text.append(text.Text("lobster", "middle_right", str(t), 24, "white"))
	for t in r_side_text:
		rs_text.append(text.Text("lobster", "middle_left", str(t), 24, "white"))
	for t in h_side_text:
		hs_text.append(text.Text("lobster", "middle_right", str(t), 24, "white"))
	for t in h_side_text:
		fin_text.append(text.Text("lobster", "middle_center", str(t), 24, "white"))
	time = pygame.time.Clock()
	image = Camera()
	while state != 0:
		t = 5000
		while t > 0 and state !=0:
			if t > 0: t -= time.tick()
			screen.blit(screen_rect, (0,0))
			screen.blit(welcome.message, welcome.position)
			# screen_rect.set_alpha(alpha)
			# alpha -= 5
			pygame.display.flip()
			state = event.check()
		t = 4000
		while t > 0 and state != 0:
			screen.blit(screen_rect, (0,0))
			if t > 0: t -= time.tick()
			i = 0
			for te in f_text:
				screen.blit(te.message, (te.position[0],(te.position[1]-40)+i))
				i += 40
			pygame.display.flip()
			state = event.check()
		t = 8000
		while t > 0 and state != 0:
			image.optimize()
			image.render()
			box = sticker_images[1]
			screen.blit(box, ((config.positions["middle_center"][0] - box.get_width()/2),(config.positions["middle_center"][1] - box.get_height()/2)))
			screen.blit(screen_rect, (0,0))
			if t > 0: t -= time.tick()
			screen_rect.set_alpha(alpha)
			alpha -= 5
			i = 0
			if len(s_text) < 1:
				screen.blit(s_text[0].message, (s_text[0].position[0],(s_text[0].position[1])+i))
			else:
				for te in s_text:
					screen.blit(te.message, (te.position[0],(te.position[1])+i))
					i += 40
			pygame.display.flip()
			state = event.check()
		chosen = False
		while chosen == False and state != 0:
			image.optimize()
			image.render()
			i = 1
			screen.blit(screen_rect, (0,0))
			for s in sticker_images:
				s_pos = s.get_rect(centerx=config.positions["middle_left"][0]+i*s.get_width()*1.2,centery = config.positions["middle_left"][1])
				if s.get_width() != 300:
					if s_pos.collidepoint(pygame.mouse.get_pos()):
						sticker_image = s
						s = pygame.transform.scale(s, (int(s.get_width()*1.05), int(s.get_height()*1.05)))
						e = pygame.event.poll()
						if e.type == pygame.MOUSEBUTTONDOWN:
							chosen = True
					screen.blit(s, s_pos)
					i += 1
			screen_rect.set_alpha(alpha)
			alpha += 15
			i = 0
			for te in r_text:
				screen.blit(te.message, (te.position[0],(te.position[1])+i))
				i += 40
			pygame.display.flip()
			state = event.check()
		t =15000
		while t > 0 and state != 0:
			image.optimize()
			image.render()
			if t > 0: t -= time.tick()
			i = 0
			for te in h_text:
				screen.blit(te.message, (te.position[0],(te.position[1])+i))
				i += 40
			screen.blit(smile, (config.positions['middle_center'][0]-smile.get_width()/2, config.positions['middle_center'][1]-smile.get_height()/3))
			pygame.display.flip()
			state = event.check()
		t = 3000
		while t > 0 and state !=0:
			image.optimize()
			image.render()
			if t > 0: t -= time.tick()
			screen.blit(correct.message, correct.position)
			screen.blit(sticker_image, (config.positions["bottom_center"][0]-sticker_image.get_width()/2,config.positions["bottom_center"][1]-sticker_image.get_height()))
			pygame.display.flip()
			state = event.check()
		correct_side = False
		while correct_side == False and state != 0:
			image.optimize()
			cv.Rectangle(image.image, (1,1), (320, 480), config.colors[config.color], 10, cv.CV_AA, 0)
			image.detectFace()
			for f in image.faces:
				side = image.side(f)
				if side == "left":
					correct_side = True
			image.render()
			i = 0
			for te in ls_text:
				screen.blit(te.message, (te.position[0]-100,(te.position[1])+i))
				i += 40
			pygame.display.flip()
			state = event.check()
			pygame.time.delay(60)
		t = 3000
		while t > 0 and state !=0:
			image.optimize()
			image.render()
			if t > 0: t -= time.tick()
			screen.blit(correct.message, correct.position)
			screen.blit(sticker_image, (config.positions["bottom_center"][0]-sticker_image.get_width()/2,config.positions["bottom_center"][1]-sticker_image.get_height()))
			pygame.display.flip()
			state = event.check()
		correct_side = False
		while correct_side == False and state != 0:
			image.optimize()
			cv.Rectangle(image.image, (320,0), (640, 480), config.colors[config.color], 10, cv.CV_AA, 0)
			image.detectFace()
			for f in image.faces:
				side = image.side(f)
				if side == "right":
					correct_side = True
			image.render()
			i = 0
			for te in rs_text:
				screen.blit(te.message, (te.position[0]+100,(te.position[1])+i))
				i += 40
			pygame.display.flip()
			state = event.check()
			pygame.time.delay(60)
		t = 3000
		while t > 0 and state !=0:
			image.optimize()
			image.render()
			if t > 0: t -= time.tick()
			screen.blit(correct.message, correct.position)
			screen.blit(sticker_image, (config.positions["bottom_center"][0]-sticker_image.get_width()/2,config.positions["bottom_center"][1]-sticker_image.get_height()))
			pygame.display.flip()
			state = event.check()
		correct_side = False
		score = 0
		while correct_side == False and state !=0:
			image.optimize()
			cv.Rectangle(image.image, (0,0), (320, 480), config.colors[config.color], 10, cv.CV_AA, 0)
			image.detectFace()
			for f in image.faces:
				side = image.side(f)
				if side == "left":
					score +=1
			if score > 20:
				correct_side = True
			image.render()
			screen.blit(smile, (config.positions['middle_left'][0], config.positions['middle_left'][1]-smile.get_height()/3))
			i = 0
			for te in hs_text:
				screen.blit(te.message, (te.position[0]-100,(te.position[1])+i))
				i += 40
			pygame.display.flip()
			state = event.check()
			pygame.time.delay(60)
		t = 3000
		while t > 0 and state !=0:
			image.optimize()
			image.render()
			if t > 0: t -= time.tick()
			screen.blit(correct.message, correct.position)
			screen.blit(sticker_image, (config.positions["bottom_center"][0]-sticker_image.get_width()/2,config.positions["bottom_center"][1]-sticker_image.get_height()))
			pygame.display.flip()
			state = event.check()
		correct_side = False
		t = 15000
		score = 0
		show_try_text = False
		s_t_t = 0
		while correct_side == False and state !=0:
			image.optimize()
			cv.Rectangle(image.image, (320,0), (640, 480), config.colors[config.color], 10, cv.CV_AA, 0)
			image.detectFace()
			t -= time.tick()
			timer = text.Text("lobster", "bottom_left", str(t/1000),48, "white")
			try_again = text.Text("lobster", "bottom_right", "Try again :(", 48, "white")
			for f in image.faces:
				side = image.side(f)
				if side == "right":
					score +=1
			if score > 20:
				correct_side = True
			image.render()
			screen.blit(timer.message, timer.position)
			screen.blit(smile, (config.positions['middle_right'][0]-smile.get_width(), config.positions['middle_right'][1]-smile.get_height()/3))
			i = 0
			for te in hs_text:
				screen.blit(te.message, (te.position[0]-400,(te.position[1])+i))
				i += 40
			if t/1000 == 0:
				t = 15000
				show_try_text = True
			if show_try_text:
				screen.blit(try_again.message, (try_again.position[0]-100, try_again.position[1]))
				s_t_t += time.tick()
			if s_t_t > 300:
				show_try_text = False
				s_t_t = 0
			pygame.display.flip()
			state = event.check()
			pygame.time.delay(60)
		while state != 0:
			i = 0
			image.optimize()
			image.render()
			for te in fin_text:
				screen.blit(te.message, (te.position[0],(te.position[1]-40)+i))
				i += 40
			screen.blit(play_button, (config.positions["middle_center"][0]-play_button.get_width()/2, config.positions["middle_center"][1]))
			e = pygame.event.poll()
			p_pos = pygame.Rect((config.positions["middle_center"][0]-play_button.get_width()/2,config.positions["middle_left"][1]), (play_button.get_width(), play_button.get_height()))
			if e.type == pygame.MOUSEBUTTONDOWN and p_pos.collidepoint(pygame.mouse.get_pos()):
				play()
			pygame.display.flip()
			state = event.check()

# Run the main program now.			
if __name__ == "__main__":
	learn()

