import pygame
from game_object import GameObject
from abc import ABC, abstractmethod


class AStatusBar(GameObject, ABC):
    def __init__(self, x, y, width, height, color, txt_color, value, surface=None):
        GameObject.__init__(self, x, y, width, height)
        self.color = color
        self.value = value
        self.txt_color = txt_color
        self.surface = surface
        self.font = pygame.font.Font('freesansbold.ttf', 12)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def update_status(self, num):
        self.value = num
        text = self.font.render(str(self.value), True, self.txt_color, self.color)
        self.surface.blit(text, (self.bounds.x, self.bounds.y))
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
    def __init__(self, x, y, width, height, color, txt_color, value):
        AStatusBar.__init__(self, x, y, width, height, color, txt_color, value)

class Clocks:
    def __init__(self, days, previous_time):
        self.days = days
        self.previous_time = previous_time

