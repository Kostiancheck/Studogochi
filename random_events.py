import pygame
from game_object import GameObject
import random as r
from abc import ABC, abstractmethod
import time

class RandomEvent(GameObject, ABC):
    def __init__(self, x, y, width, height, screen, days, gamer, size_of_window):
        super().__init__(x, y, width, height)
        self.screen = screen
        self.days = days
        self.gamer = gamer
        self.size_of_window = size_of_window

    @abstractmethod
    def random_event(self):
        pass

    @staticmethod
    def draw(self, str):
        pass

class RandomEventHealth(RandomEvent):
    """In this class, especially in random_event method you can 
    orginize events that can cause minus to health of student"""
    def __init__(self, x, y, width, height, screen, days, gamer, size_of_window):
        super().__init__(x, y, width, height, screen, days, gamer, size_of_window)

    def random_event(self):
        if self.days.days % 7 == 0 and r.randint(1,3)%2==0:
            self.gamer.update_statistic('health', -5)
            self.gamer.update_statistic('alcohol', 6)
            self.draw()
            time.sleep(1.5)
    
    def draw(self):
            surf = pygame.image.load('images/backgrounds/gameover_back.png')
            surf = pygame.transform.scale(surf, (self.width, self.height))
            a = (self.size_of_window[0]-self.width)/2
            b = (self.size_of_window[1]-self.height)/2
            rect = surf.get_rect(bottomright=(self.width+a, self.height+b))
            self.screen.blit(surf, rect)
            font_1 = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 50)
            game_over_str = font_1.render("Incident", True,
                                            (25,25,25),
                                            (255,255,255))
            game_over_str.set_colorkey((255,255,255))
            self.screen.blit(game_over_str, (a+(self.width/2)-110, b+20))
            font_2 = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 25)
            game_over_why = font_2.render('You drank too much', True,
                                            (25,25,25),
                                            (255,255,255))
            game_over_why.set_colorkey((255,255,255))
            self.screen.blit(game_over_why, (a+(self.width/2)-120, b+400))
            game_over_exit = font_2.render("Here you got alcohol intocsication", True,
                                            (25,25,25),
                                            (255,255,255))
            game_over_exit.set_colorkey((255,255,255))
            self.screen.blit(game_over_exit, (a+(self.width/2)-190, b+450))
            pygame.display.update()
        
        