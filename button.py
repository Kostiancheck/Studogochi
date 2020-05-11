import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from interface_draw import IDraw
from statusbar import StatusHealth
import time


class AButton(GameObject, IDraw):
    """This is abstract class of buttons for making new buttons to control student"""

    def __init__(self,  x, y, width, height, image, characteristic):
        super().__init__(x, y, width, height)
        self.image = image
        self.characteristic = characteristic

    def draw(self, surface):
        images = pygame.image.load(self.image)
        rect = images.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        surface.blit(images, rect)

    def push(self, mouse_x, mouse_y, mouse_click, surface):
        if (self.bounds.x > mouse_x > self.bounds.x - self.width and
                self.bounds.y > mouse_y > self.bounds.y - self.height and
                mouse_click == 1):

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
