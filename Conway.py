# Charlie DeGennaro

import pygame
import pygame.gfxdraw
from random import random
pygame.init()


screenSquare = 808
background = (255, 255, 255)

def drawCluster4(surface,x,y):
	o = 1
	pygame.gfxdraw.pixel(surface, x, y, (0, 0, 255))
	pygame.gfxdraw.pixel(surface, x+o, y, (0, 0, 255))
	pygame.gfxdraw.pixel(surface, x, y+o, (0, 0, 255))
	pygame.gfxdraw.pixel(surface, x+o, y+o, (0, 0, 255))

def drawCluster(surface, x, y):
	o = 2
	drawCluster4(surface, x, y)
	drawCluster4(surface,x+o, y)
	drawCluster4(surface, x, y+o)
	drawCluster4(surface, x+o, y+o)

def drawClusterToGrid(surface, x, y):
	o = 3
	drawCluster(surface, x * 8 + o, y * 8 + o)

#def drawGrid()


# Clicking on an pixel will turn it on or off, and store it's value in a 2d boolean array based on the coords of the click


win = pygame.display.set_mode([screenSquare, screenSquare], pygame.RESIZABLE)

pygame.display.set_caption("Conway")
xx = 0 
yy = 0
run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	xx = int(random() * 100)		
	yy = int(random() * 100)
	
	win.fill(background)
	
	
	drawClusterToGrid(win, xx, yy)

	pygame.display.update()


pygame.quit()

