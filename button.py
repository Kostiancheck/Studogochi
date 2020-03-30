import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import StatusHealth


class AButton(GameObject, ABC):
    """This is abstract class of buttons for making new buttons to control student"""

    def __init__(self, x, y, radius, color):
        GameObject.__init__(self, x, y, radius * 2, radius * 2)
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.bounds.x, self.bounds.y),
                           self.radius)  # bounds is instance of class Rect wich is used in GameObject

    @abstractmethod
    def increase(self, attribute):
        pass


class ButtonHealth(AButton):
    """This button contols student's health"""

    def __init__(self, x, y, radius, color):
        AButton.__init__(self, x, y, radius, color)

    def increase(self, surface):
        StatusHealth.update_status(10, surface, surface)
