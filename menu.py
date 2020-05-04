import pygame
from game_object import GameObject
from exception import *

class Menu:
    def __init__(self, x, y, width, height, text_color, color, screen, clocks):
        GameObject.__init__(self, x, y, width, height)
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.text_color = text_color
        self.color = color
        self.open = False
        self.screen = screen
        self.clocks = clocks


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def open_menu(self, background_image, trigger):
        if trigger:
            self.draw(self.screen)
            data = list()
            data.append(["F1", "Show Help"])
            data.append(["Esc", "Exit Game"])
            data.append(['You alived: ', str(self.clocks.days)+' days in our wonderful university :)'])
            for i, text in enumerate(data):
                self.screen.blit(self.font.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
                self.screen.blit(self.font.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
            pygame.display.update()
        else:
            self.screen.blit(background_image, (0, 0))
            pygame.display.update()
            


class InfoGameover:
    def __init__(self, x, y, width, height, color, txt_color, value, gamer, clocks, screen ,surface=None):
        GameObject.__init__(self, x, y, width, height)
        self.color = color
        self.value = value
        self.txt_color = txt_color
        self.surface = surface
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.image = 'images/game_over.jpg'
        self.game_end = False
        self.gamer = gamer
        self.clocks = clocks
        self.screen = screen

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def update_status(self, char, num):
        self.is_end(char, num)
    
    def is_end(self, stat, num):
        try:
            if stat == 'grades':
                if int(num) < 60 and int(self.clocks.days) >= 365:
                    raise NegativeStatisticGrades(stat)
                        
            elif int(num) <= 0:
                raise NegativeStatistic(stat)
        except NegativeStatisticGrades as n:
            self.draw(self.screen)
            game_over_str = self.font.render("В армии увидимся", True,
                                                    self.txt_color,
                                                    self.color)
            self.screen.blit(game_over_str, (self.bounds.x+60, self.bounds.y+5))
            game_over_why = self.font.render("Надо было учиться лол", True,
                                                    self.txt_color,
                                                    self.color)
            self.screen.blit(game_over_why, (self.bounds.x+40, self.bounds.y+40)) 
            surf = pygame.image.load(self.image)
                        
            self.screen.blit(surf, (self.bounds.x+100, self.bounds.y+70))
            game_over_exit = self.font.render("Presss Esc to exit", True,
                                                self.txt_color,
                                                    self.color)
            self.screen.blit(game_over_exit, (self.bounds.x+70, self.bounds.y+200)) 
            self.game_end = True
            pygame.display.update()
        except NegativeStatistic as m:
            self.draw(self.screen)
            game_over_str = self.font.render("GAMEOVER", True,
                                                self.txt_color,
                                                self.color)
            self.screen.blit(game_over_str, (self.bounds.x+90, self.bounds.y+5))
            game_over_why = self.font.render("because of {}".format(m), True,
                                                self.txt_color,
                                                self.color)
            self.screen.blit(game_over_why, (self.bounds.x+60, self.bounds.y+40)) 
            surf = pygame.image.load(self.image)
                    
            self.screen.blit(surf, (self.bounds.x+100, self.bounds.y+80))
            game_over_exit = self.font.render("Presss Esc to exit", True,
                                                self.txt_color,
                                                self.color)
            self.screen.blit(game_over_exit, (self.bounds.x+70, self.bounds.y+200)) 
            self.game_end = True
            pygame.display.update()