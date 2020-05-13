import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from interface_draw import IDraw
import datetime


class AStatusBar(GameObject, IDraw):
    def __init__(self, x, y, width, height, txt_color, value, background=None, characteristic=None,
                 surface=None):
        super().__init__(x, y, width, height)
        self.value = value
        self.txt_color = txt_color
        self.font = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 40)
        self.background = background
        self.characteristic = characteristic
        self.surface = surface

    """ЭТО АБСТРАКТНЫЙ КЛАСС, ПОТОМУ ЧТО КАЖДЫЙ СТАТУСБАР В ИДЕАЛЕ ОТРИСОВЫВАЕТСЯ ПО РАЗНОМУ"""

    def draw(self):
        statusbar_background = pygame.image.load(self.background)
        statusbar_background = pygame.transform.scale(statusbar_background, (self.width, self.height))
        rect = statusbar_background.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        self.surface.blit(statusbar_background, rect)

        value = self.font.render(self.characteristic+': '+str(self.value), True, self.txt_color)
        self.surface.blit(value, (self.bounds.x - self.width + 10, self.bounds.y - self.height))

    def update_status(self, num):
        self.value = num
        text = self.font.render(str(self.value), True, self.txt_color)
        self.surface.blit(text, (self.bounds.x + 13, self.bounds.y))
        pygame.display.update()


"""IN FUNCTION DRAW IN THIRD PARAMETR IS TUPLE WHERE FIRST TWO ARGUMENTS ARE X AND Y COORDINATES OF 
TOP RIGHT EDGE AND NEXT TWO PARAMETRS IS WIDTH AND HEIGHT"""


class StatusHealth(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, characteristic, surface):
        super().__init__(x, y, width, height, txt_color, value, background, characteristic, surface)


class StatusFatigue(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, characteristic, surface):
        super().__init__(x, y, width, height, txt_color, value, background, characteristic, surface)


class StatusGrades(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, characteristic, surface):
        super().__init__(x, y, width, height, txt_color, value, background, characteristic, surface)


class StatusMoney(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, characteristic, surface):
        super().__init__(x, y, width, height, txt_color, value, background, characteristic, surface)


class StatusAlcohol(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, characteristic, surface):
        super().__init__(x, y, width, height, txt_color, value, background, characteristic, surface)


# ADDED
class Timer(AStatusBar):
    def __init__(self, x, y, width, height, txt_color, value, background, surface=None):
        super().__init__(x, y, width, height, txt_color, value)
        self.background = background
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.surface = surface

    def draw(self, timer_value, val):
        surf = pygame.image.load(self.background)
        surf = pygame.transform.scale(surf, (self.width, self.height))
        rect = surf.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        self.surface.blit(surf, rect)
        if int(val) < 10:
            text = self.font.render(str(timer_value), True, self.txt_color)
            self.surface.blit(timer_value, (self.bounds.x - (10 + self.width / 2), self.bounds.y - 45))
        elif int(val) < 100:
            text = self.font.render(str(timer_value), True, self.txt_color)
            self.surface.blit(timer_value, (self.bounds.x - (19 + self.width / 2), self.bounds.y - 45))
        else:
            text = self.font.render(str(timer_value), True, self.txt_color)
            self.surface.blit(timer_value, (self.bounds.x - (27 + self.width / 2), self.bounds.y - 45))
        pygame.display.update()


class Clocks:
    def __init__(self, days, previous_time):
        self.days = days
        self.previous_time = previous_time
