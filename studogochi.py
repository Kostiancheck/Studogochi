import pygame
from button import *
from abc import ABC
from statusbar import *
from student import Student
from game import Game

WHITE = (255, 255, 255)

class Studogochi(Game):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background_image = pygame.image.load('images/background.jpeg')
        self.screen.blit(self.background_image, (0, 0))
        self.clock = pygame.time.Clock()
        self.objects = []
        self.button_health = ButtonHealth(50, 50, 25, WHITE)
        self.button_fatigue = ButtonFatigue(50, 150, 25, WHITE)
        pygame.init()
        self.statusbar_health = StatusHealth(700, 20, 50, 20, (220, 20, 60), 100, WHITE)
        self.statusbar_fatigue = StatusFatigue(700, 50, 50, 20, (0, 255, 0), 100, WHITE)

        self.gamer = Student(500, 400, 100, 200, 'Bob', 'images/student.jpeg', [self.statusbar_health, self.statusbar_fatigue])

    def draw_all(self):
        self.statusbar_health.draw(self.screen)
        statusbar_health_value = self.statusbar_health.font.render(str(self.statusbar_health.value), True, self.statusbar_health.txt_color,
                                            self.statusbar_health.color)
        self.screen.blit(statusbar_health_value, (self.statusbar_health.bounds.x, self.statusbar_health.bounds.y))

        self.statusbar_fatigue.draw(self.screen)
        statusbar_fatigue_value = self.statusbar_fatigue.font.render(str(self.statusbar_fatigue.value), True,
                                                                self.statusbar_fatigue.txt_color,
                                                                self.statusbar_fatigue.color)
        self.screen.blit(statusbar_fatigue_value, (self.statusbar_fatigue.bounds.x, self.statusbar_fatigue.bounds.y))

        self.gamer.draw(self.screen)

        self.button_health.draw(self.screen)
        self.button_fatigue.draw(self.screen)
        pygame.display.update()

    def run(self):

        pygame.display.set_caption('Studogochi')
        run = True
        while run:
            self.draw_all()
            self.clock.tick(60)
            pygame.time.delay(100)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if event.type == pygame.QUIT:
                    run = False

                elif (self.button_health.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_health.update_status(10, self.screen)

                elif (self.button_fatigue.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_fatigue.update_status(10, self.screen)

