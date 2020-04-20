# Charlie DeGennaro

import pygame

pygame.init()


screenSquare = 500
background = (255, 255, 255)



# Clicking on and pixel will turn it on or off, and store it's value in a 2d boolean array based on the coords of the click

























win = pygame.display.set_mode([screenSquare, screenSquare])

pygame.display.set_caption("Conway")

run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False




	win.fill(background)

	pygame.display.update()


pygame.quit()













