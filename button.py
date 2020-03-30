import pygame
from game_object import GameObject
from abc import ABC,abstractmethod

class AButton(GameObject,ABC):
  def __init__(self,x,y,radius,color):
    GameObject.__init__(self,x,y,radius * 2,radius * 2)
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color

  
  def draw(self,surface):
     pygame.draw.circle(surface, self.color, (self.x,self.y),self.radius)

  @abstractmethod
  def increase(self,attribute):
    pass


class ButtonHealth(AButton):
  def __init__(self,x,y,radius,color):
    AButton.__init__(self,x,y,radius,color)

  def increase(self,attribute):
    pass




