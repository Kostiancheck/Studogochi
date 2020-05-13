import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from interface_draw import IDraw
from statusbar import StatusHealth
import time


class AButton(GameObject, IDraw):
    """This is abstract class of buttons for making new buttons to control student"""

    def __init__(self, x, y, width, height, image, characteristic, surface):
        super().__init__(x, y, width, height)
        self.image = image
        self.characteristic = characteristic
        self.surface = surface


    def draw(self):
        button_icon = pygame.image.load(self.image)
        button_icon = pygame.transform.scale(button_icon, (self.width, self.height))
        rect = button_icon.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        self.surface.blit(button_icon, rect)

    def in_circle(self, mouse_x, mouse_y):
        if ((mouse_x - self.bounds.x + self.width / 2) ** 2 + \
                (mouse_y - self.bounds.y + self.height / 2) ** 2 <= (self.height/2) ** 2):
            return True

    def push(self, mouse_x, mouse_y, mouse_click, surface):
        if (mouse_click == 1 and self.in_circle(mouse_x, mouse_y)):
            # Change button's color
            # pushed_mouse_color = (0, 191, 255)
            # self.color, pushed_mouse_color = pushed_mouse_color, self.color
            # self.draw(surface)
            # pygame.display.update()
            # time.sleep(0.2)
            # self.color, pushed_mouse_color = pushed_mouse_color, self.color
            # self.draw(surface)
            # pygame.display.update()
            return True

    @abstractmethod
    def increase(self, value, gamer):
        pass


class Button(AButton):
    def increase(self, value, gamer):
        gamer.update_statistic(self.characteristic, value)


class GradesButton(AButton):
    """This method will be changed in (not) nearest future"""

    def increase(self, value, gamer):
        gamer.update_grades(self.characteristic, value)
