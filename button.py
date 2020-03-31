import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import StatusHealth
import time


class AButton(GameObject, ABC):
    """This is abstract class of buttons for making new buttons to control student"""

    def __init__(self, x, y, radius, color):
        GameObject.__init__(self, x, y, radius * 2, radius * 2)
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.bounds.x, self.bounds.y),
                           self.radius)  # bounds is an instance of class Rect wich is used in GameObject

    def push(self, mouse_x, mouse_y, mouse_click, surface):
        if (self.bounds.x + self.radius > mouse_x > self.bounds.x - self.radius and
              self.bounds.y + self.radius > mouse_y > self.bounds.y - self.radius and
              mouse_click == 1):

            # Change button's color
            pushed_mouse_color = (0, 191, 255)
            self.color, pushed_mouse_color = pushed_mouse_color, self.color
            self.draw(surface)
            pygame.display.update()
            time.sleep(0.2)
            self.color, pushed_mouse_color = pushed_mouse_color, self.color
            self.draw(surface)
            pygame.display.update()

            return True


    @abstractmethod
    def increase(self, attribute):
        pass


class ButtonHealth(AButton):
    """This button contols student's health"""

    def __init__(self, x, y, radius, color):
        AButton.__init__(self, x, y, radius, color)

    def increase(self, surface):
        StatusHealth.update_status(10, surface)
