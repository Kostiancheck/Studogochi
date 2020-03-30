import pygame
from button import ButtonHealth
from abc import ABC
from statusbar import StatusHealth


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.jpeg')
pygame.display.set_caption('Studogochi')

WHITE = (255,255,255)
run = True
while run:
	screen.blit(background_image, (0, 0))
    

    #THIS SECTION IS FOR STUDENT

    

    #THIS SECTION IS FOR STATUSBARS
	statusbar_health = StatusHealth(700,20,50,20,(220,20,60),100,WHITE)
	statusbar_health.draw_rect(screen)
	text = statusbar_health.font.render(str(statusbar_health.value), True, statusbar_health.txt_color, statusbar_health.color)
	screen.blit(text,(statusbar_health.bounds.x,statusbar_health.bounds.y))


    #THIS SECTION IS FOR BUTTONS
	button_health = ButtonHealth(50,50,25,WHITE)
	button_health.draw(screen)




	pygame.display.update()
	clock.tick(60)
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			statusbar_health.update_status(10,screen)
			print(statusbar_health.value)

pygame.quite()


