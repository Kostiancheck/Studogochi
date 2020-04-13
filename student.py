import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import *

class Student(GameObject,ABC):
	def __init__(self,x,y,width,height,name,image,statistics):
		GameObject.__init__(self,x,y,width,height)
		self._name = name 
		self.image = image
		self.__statistics = statistics
		self.font = pygame.font.Font('freesansbold.ttf', 25)

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		print("You can't do this operation!")
		return 0

	def draw(self,surface):
		surf = pygame.image.load(self.image)
		rect = surf.get_rect(bottomright=(self.bounds.x, self.bounds.y))
		surface.blit(surf, rect)
		text = self.font.render(str(self._name), True, (255, 0, 0),
								(255, 255, 255))
		surface.blit(text, (self.bounds.x - 130, self.bounds.y))
