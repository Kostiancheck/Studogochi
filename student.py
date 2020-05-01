import pygame
from game_object import GameObject
from abc import ABC, abstractmethod
from statusbar import *


class Student(GameObject, ABC):
    def __init__(self, x, y, width, height, name, image):
        GameObject.__init__(self, x, y, width, height)
        self._name = name
        self.image = image
        self.statistics = {'health': 100,
                           'fatigue': 100,
                           # Сделать много подпунтков в пункте "Grades"
                           # 'Grades': {'Матеша': 0,
                           # 		'ФП': 0},
                           'grades': 60,
                           'money': 1000,
                           'alcohol': 10,  # ТУТ БЫЛО 10 Алкоголь записывать в % (процент спирта в крови)
                           }
        self.__subscribers = {}
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def subscribe(self, characteristic, subscriber, ):
        self.__subscribers[characteristic] = subscriber

    def update_grades(self, grade):
        '''В перспективе это будет отдельный от update_statistic метод
        который будет принимать название предмета и оценку'''
        self.statistics['grades'] += grade
        self.__subscribers['grades'].update_status(self.statistics['grades'])

    def update_statistic(self, characteristic, value):
        self.statistics[characteristic] += value
        self.__subscribers[characteristic].update_status(self.statistics[characteristic])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("You can't do this operation!")
        return 0

    def draw(self, surface):
        surf = pygame.image.load(self.image)
        rect = surf.get_rect(bottomright=(self.bounds.x, self.bounds.y))
        surface.blit(surf, rect)
        text = self.font.render(str(self._name), True, (255, 0, 0),
                                (255, 255, 255))
        surface.blit(text, (self.bounds.x - 130, self.bounds.y))
