import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import *

class Student(GameObject,ABC):
	def __init__(self,x,y,width,height,name,image,statistics):
		GameObject.__init__(self,x,y,width,height)
		self._name = name 
		self.image = image
		self.statistics = statistics

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		print("You can't do this operation!")
		return 0


