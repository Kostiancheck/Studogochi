import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import StatusHealth
import time


class AButton(GameObject, ABC):
    """This is abstract class of buttons for making new buttons to control student"""

    def __init__(self, x, y, width, height, image):
        GameObject.__init__(self, x, y, width, height)
        self.image = image

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
    def increase(self, attribute):
        pass


class ButtonHealth(AButton):
    """This button contols student's health"""

    def __init__(self,  x, y, width, height, image):
        AButton.__init__(self, x, y, width, height, image)

    def increase(self, surface):
        StatusHealth.update_status(10, surface)

class ButtonFatigue(AButton):
    """This button contols student's health"""

    def __init__(self, x, y, width, height, image):
        AButton.__init__(self, x, y, width, height, image)

    def increase(self, surface):
        StatusFatigue.update_status(5, surface)


class ButtonGrades(AButton):
    """This button contols student's grades """

    def __init__(self, x, y, width, height, image):
        AButton.__init__(self, x, y, width, height, image)

    def increase(self, surface):
        StatusGrades.update_status(5, surface)

class ButtonMoney(AButton):
    """This button contols student's money """

    def __init__(self, x, y, width, height, image):
        AButton.__init__(self, x, y, width, height, image)

    def increase(self, surface):
        StatusMoney.update_status(15, surface)

class ButtonAlcohol(AButton):
    """This button contols student's alcohol """

    def __init__(self, x, y, width, height, image):
        AButton.__init__(self, x, y, width, height, image)

    def increase(self, surface):
        StatusAlcohol.update_status(15, surface)