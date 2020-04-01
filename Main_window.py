import pygame
from button import *
from abc import ABC
from statusbar import *
from student import Student


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.jpeg')
pygame.display.set_caption('Studogochi')

WHITE = (255, 255, 255)

screen.blit(background_image, (0, 0))


# THIS SECTION IS FOR STATUSBARS
statusbar_health = StatusHealth(700, 20, 50, 20, (220, 20, 60), 100, WHITE)
statusbar_health.draw_rect(screen)
text = statusbar_health.font.render(str(statusbar_health.value), True, statusbar_health.txt_color,
                                    statusbar_health.color)
screen.blit(text, (statusbar_health.bounds.x, statusbar_health.bounds.y))

statusbar_fatigue = StatusFatigue(700, 50, 50, 20, (0,255,0), 100, WHITE)
statusbar_fatigue.draw_rect(screen)
text = statusbar_fatigue.font.render(str(statusbar_fatigue.value), True, statusbar_fatigue.txt_color,
                                    statusbar_fatigue.color)
screen.blit(text, (statusbar_fatigue.bounds.x, statusbar_fatigue.bounds.y))



# THIS SECTION IS FOR STUDENT
gamer = Student(500,400,100,200,'Bob','images/student.jpeg',[statusbar_health,statusbar_fatigue])
gamer.draw(screen)



# THIS SECTION IS FOR BUTTONS
button_health = ButtonHealth(50, 50, 25, WHITE)
button_health.draw(screen)


button_fatigue = ButtonFatigue(50, 150, 25, WHITE)
button_fatigue.draw(screen)

pygame.display.update()

run = True
while run:
    clock.tick(60)
    pygame.time.delay(100)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if event.type == pygame.QUIT:
            run = False

        elif (button_health.push(pos[0], pos[1], click[0], screen) is True):
            statusbar_health.update_status(10, screen)

        elif (button_fatigue.push(pos[0], pos[1], click[0], screen) is True):
            statusbar_fatigue.update_status(10, screen)