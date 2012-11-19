#!/usr/bin/env python3
import sys
import pygame
pygame.init()

width = height = 300
Xs_turn = True
black = (0, 0, 0)
blue = (0, 18, 194)
red = (255, 165, 0)
size = (height+width)/2/5 #size of "X" and "o" is based on overall game size
running = True
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Tic, Tac, Toe!")
screen = pygame.display.set_mode((width, height))

class ai(object):
	def check_if_allowed(area):
		if state[ai.transform_to_array(area)] == 0:
			return True
		else:
			return False
			
	def set_state(area, value):
		state[ai.transform_to_array(area)] = value #sets the state of a field
		
	def transform_to_array(area): #transforms given tupel into index of state array
		re = (3*(area[1]-1)) + (area[0]-1) 
		#print(re)
		return(re)

		
class mouse_handler(object): 
	def klickarea(): #returns which area was klicked
		#print(pygame.mouse.get_pos())
		mouse_position = pygame.mouse.get_pos()
		column = 0
		if mouse_position[0] <= width/3:
			column = 1
		elif mouse_position[0] <= (width / 3) * 2:
			column = 2
		else: 
			column = 3
		
		if mouse_position[1] <= height/3:
			line = 1
		elif mouse_position[1] <= (height / 3) * 2:
			line = 2
		else: 
			line = 3
		field_position = column, line
		#print(field_position)	
		return(field_position)
			
class draw(object):
	def field():
		color = black
		pygame.draw.line(screen, (color), ((width/3)-2, height), ((width/3)-2, 0), 5) #vertical lines
		pygame.draw.line(screen, (color), (((width/3)*2), height), (((width/3)*2), 0), 5) #vertical lines
		pygame.draw.line(screen, (color), (0, height/3), (width, (height/3)), 5) #horizontal lines
		pygame.draw.line(screen, (color), (0, (height/3)*2), (width, (height/3)*2), 5) #horizontal lines
		print("Draw the field")
		
	def X(area):	
		color = red
		#print(area, "x")
		xoff = width/3*(area[0]-1)+((width/3 - size)/2)
		yoff = height/3*(area[1]-1)+((height/3 - size)/2)
		pygame.draw.line(screen, (color), (0 + xoff, size + yoff), (size + xoff, 0 + yoff), 5)
		pygame.draw.line(screen, (color), (0 + xoff, 0 + yoff), (size + xoff, size + yoff), 5)
		
	def O(area):
		color = blue
		#print(area, "o")
		xoff = (width/3)*(area[0]-1) + (height+width)/2/6 
		yoff = (height/3)*(area[1]-1) + (height+width)/2/6
		pos = (int(xoff), int(yoff))
		pygame.draw.circle(screen, color, pos, int((size/2)), 5)
		
		
screen.fill((255, 255, 255))
draw.field()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if pygame.mouse.get_pressed() == (True, False, False): #if player clicks 
			if Xs_turn == True:
				new_x = mouse_handler.klickarea()
				if ai.check_if_allowed(new_x): #if field is free
					draw.X(new_x)
					ai.set_state(new_x, -1)
					print("x", Xs_turn)
					Xs_turn = False
					
			elif Xs_turn == False:
				new_o = mouse_handler.klickarea()
				if ai.check_if_allowed(new_o):
					draw.O(new_o)
					ai.set_state(new_o, 1)
					print("o", Xs_turn)
					Xs_turn = True
					
	pygame.display.flip()
	
	
