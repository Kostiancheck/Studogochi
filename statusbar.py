import pygame
from game_object import GameObject
from abc import ABC, abstractmethod


class AStatusBar(GameObject, ABC):
    def __init__(self, x, y, width, height, color, value, txt_color):
        GameObject.__init__(self, x, y, width, height)
        self.color = color
        self.value = value
        self.txt_color = txt_color
        self.font = pygame.font.Font('freesansbold.ttf', 12)

    def draw_rect(self, surface):
        pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def update_status(self, num, surface):
        self.value += num
        text = self.font.render(str(self.value), True, self.txt_color, self.color)
        surface.blit(text, (self.bounds.x, self.bounds.y))
        pygame.display.update()


"""IN FUNCTION DRAW IN THIRD PARAMETR IS TUPLE WHERE FIRST TWO ARGUMENTS ARE X AND Y COORDINATES OF 
TOP RIGHT EDGE AND NEXT TWO PARAMETRS IS WIDTH AND HEIGHT"""


class StatusHealth(AStatusBar):
    def __init__(self, x, y, width, height, color, value, txt_color):
        AStatusBar.__init__(self, x, y, width, height, color, value, txt_color)

class StatusFatigue(AStatusBar):
    def __init__(self, x, y, width, height, color, value, txt_color):
        AStatusBar.__init__(self, x, y, width, height, color, value, txt_color)
