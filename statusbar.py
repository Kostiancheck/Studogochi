import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from interface_draw import IDraw
import datetime


class AStatusBar(GameObject, IDraw):
    def __init__(self, x, y, width, height, color, txt_color, value, surface=None):
        super().__init__(x, y, width, height)
        self.color = color
        self.value = value
        self.txt_color = txt_color
        self.surface = surface
        self.font = pygame.font.Font('freesansbold.ttf', 12)
    """ЭТО АБСТРАКТНЫЙ КЛАСС, ПОТОМУ ЧТО КАЖДЫЙ СТАТУСБАР В ИДЕАЛЕ ОТРИСОВЫВАЕТСЯ ПО РАЗНОМУ"""
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))
        value = self.font.render(str(self.value), True, self.txt_color, self.color)
        surface.blit(value, (self.bounds.x + 13, self.bounds.y))

    def update_status(self, num):
        self.value = num
        text = self.font.render(str(self.value), True, self.txt_color, self.color)
        self.surface.blit(text, (self.bounds.x+13, self.bounds.y))
        pygame.display.update()


"""IN FUNCTION DRAW IN THIRD PARAMETR IS TUPLE WHERE FIRST TWO ARGUMENTS ARE X AND Y COORDINATES OF 
TOP RIGHT EDGE AND NEXT TWO PARAMETRS IS WIDTH AND HEIGHT"""


class StatusHealth(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, surface):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value, surface)

class StatusFatigue(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, surface):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value, surface)

class StatusGrades(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, surface):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value, surface)

class StatusMoney(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, surface):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value, surface)

class StatusAlcohol(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, surface):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value, surface)

#ADDED
class Timer(AStatusBar):
    def __init__(self, x, y, width, height, color, txt_color, value, backgound):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value)
        self.backgound = backgound
        self.font = pygame.font.Font('freesansbold.ttf', 30)
    
    def draw(self, surface, timer_value):
        surf = pygame.image.load(self.backgound)
        surf = pygame.transform.scale(surf, (self.width, self.height))
        rect = surf.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        surface.blit(surf, rect)
        text = self.font.render(str(timer_value), True, self.txt_color, self.color)
        surface.blit(timer_value, (self.bounds.x-70, self.bounds.y-50))
        pygame.display.update()

class Clocks:
    def __init__(self, days, previous_time):
        self.days = days
        self.previous_time = previous_time

