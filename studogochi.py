import pygame
from button import *
from abc import ABC
from statusbar import *
from student import Student
from game import Game
import datetime
import time

WHITE = (255, 255, 255)
TIMER_DAYS = 0.5   #ЭТО ОТВЕЧАЕТ ЗА БЫСТРОТУ ПРОТЕКАНИЯ ДНЕЙ 

class Studogochi(Game):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background_image = pygame.image.load('images/background.jpeg')
        self.screen.blit(self.background_image, (0, 0))
        self.clock = pygame.time.Clock()
        self.objects = []
        self.button_health = ButtonHealth(50, 50, 25, WHITE)
        self.button_fatigue = ButtonFatigue(50, 125, 25, WHITE)
        self.button_grades = ButtonGrades(50, 200, 25, WHITE)
        self.button_money = ButtonMoney(50, 275, 25, WHITE)
        self.button_alcohol = ButtonAlcohol(50, 350, 25, WHITE, )
        pygame.init()
        self.statusbar_health = StatusHealth(700, 20, 50, 20, (220, 20, 60), 100, WHITE)
        self.statusbar_fatigue = StatusFatigue(700, 50, 50, 20, (0, 100, 0), 100, WHITE)
        self.statusbar_grades = StatusGrades(700, 80, 50, 20, (0, 128, 128), 10, WHITE)
        self.statusbar_money = StatusMoney(700, 110, 50, 20, (255, 140, 0), 100, WHITE)
        self.statusbar_alcohol = StatusAlcohol(700, 140, 50, 20, (0, 0, 102), 50, WHITE)
        self.timer = Timer(370, 10, 55, 25, (255,255,255), 0, (0, 0, 0)) #ADDED
        self.clocks = Clocks(1, datetime.datetime.now())
        self.gamer = Student(500, 400, 100, 200, 'Bob', 'images/student.jpeg')
        self.HEALTH_DECREASE = pygame.USEREVENT
        self.FATIGUE_DECREASE = pygame.USEREVENT + 1
        self.MONEY_DECREASE = pygame.USEREVENT + 2
        self.ALCOHOL_DECREASE = pygame.USEREVENT + 3

    def draw_all(self):
        self.statusbar_health.draw(self.screen)
        statusbar_health_value = self.statusbar_health.font.render(str(self.statusbar_health.value), True,
                                                                   self.statusbar_health.txt_color,
                                                                   self.statusbar_health.color)
        self.screen.blit(statusbar_health_value, (self.statusbar_health.bounds.x, self.statusbar_health.bounds.y))

        self.statusbar_fatigue.draw(self.screen)
        statusbar_fatigue_value = self.statusbar_fatigue.font.render(str(self.statusbar_fatigue.value), True,
                                                                     self.statusbar_fatigue.txt_color,
                                                                     self.statusbar_fatigue.color)
        self.screen.blit(statusbar_fatigue_value, (self.statusbar_fatigue.bounds.x, self.statusbar_fatigue.bounds.y))

        self.statusbar_grades.draw(self.screen)
        statusbar_grades_value = self.statusbar_grades.font.render(str(self.statusbar_grades.value), True,
                                                                   self.statusbar_grades.txt_color,
                                                                   self.statusbar_grades.color)
        self.screen.blit(statusbar_grades_value, (self.statusbar_grades.bounds.x, self.statusbar_grades.bounds.y))

        self.statusbar_money.draw(self.screen)
        statusbar_money_value = self.statusbar_money.font.render(str(self.statusbar_money.value), True,
                                                                 self.statusbar_money.txt_color,
                                                                 self.statusbar_money.color)
        self.screen.blit(statusbar_money_value, (self.statusbar_money.bounds.x, self.statusbar_money.bounds.y))

        self.statusbar_alcohol.draw(self.screen)
        statusbar_alcohol_value = self.statusbar_alcohol.font.render(str(self.statusbar_alcohol.value), True,
                                                                     self.statusbar_alcohol.txt_color,
                                                                     self.statusbar_alcohol.color)
        self.screen.blit(statusbar_alcohol_value, (self.statusbar_alcohol.bounds.x, self.statusbar_alcohol.bounds.y))

        #TIMER 
        elapsedTime = datetime.datetime.now() - self.clocks.previous_time
        x = divmod(elapsedTime.total_seconds(), 60)
        if int(x[1]) < TIMER_DAYS:
            pass
        else:
            self.timer.draw(self.screen)
            self.clocks.days += 1
            timer_value = self.timer.font.render(str(self.clocks.days)+'  days', True,
                                                self.timer.txt_color,
                                                self.timer.color)
            self.screen.blit(timer_value, (self.timer.bounds.x, self.timer.bounds.y))
            self.clocks.previous_time = datetime.datetime.now()

        self.gamer.draw(self.screen)

        self.button_health.draw(self.screen)
        self.button_fatigue.draw(self.screen)
        self.button_grades.draw(self.screen)
        self.button_money.draw(self.screen)
        self.button_alcohol.draw(self.screen)
        pygame.display.update()

    def run(self):

        pygame.display.set_caption('Studogochi')
        run = True
        pygame.time.set_timer(self.HEALTH_DECREASE, 5000)
        pygame.time.set_timer(self.FATIGUE_DECREASE, 8000)
        pygame.time.set_timer(self.MONEY_DECREASE, 10000)
        pygame.time.set_timer(self.ALCOHOL_DECREASE, 12000)

        while run:
            self.draw_all()
            self.clock.tick(60)
            # pygame.time.delay(100) #я не знаю зачем нам нужна это строчка

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if event.type == pygame.QUIT:
                    run = False

                # Уменьшаем значения
                elif event.type == pygame.USEREVENT:
                    self.statusbar_health.update_status(-5, self.screen)
                    self.statusbar_fatigue.update_status(-8, self.screen)
                    self.statusbar_money.update_status(-7, self.screen)
                    self.statusbar_alcohol.update_status(-6, self.screen)

                # Нажатие кнопок
                elif (self.button_health.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_health.update_status(10, self.screen)
                elif (self.button_fatigue.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_fatigue.update_status(10, self.screen)
                elif (self.button_grades.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_grades.update_status(2, self.screen)
                elif (self.button_money.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_money.update_status(10, self.screen)
                elif (self.button_alcohol.push(pos[0], pos[1], click[0], self.screen) is True):
                    self.statusbar_alcohol.update_status(10, self.screen)
