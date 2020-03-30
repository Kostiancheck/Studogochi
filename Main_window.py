import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.jpeg')

run = True
while run:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quite()


