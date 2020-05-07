import pygame
from button import *
from abc import ABC
from statusbar import *
from student import Student
from game import Game
import datetime
import time
from menu import *

WHITE = (255, 255, 255)
TIMER_DAYS = 5  # ЭТО ОТВЕЧАЕТ ЗА БЫСТРОТУ ПРОТЕКАНИЯ ДНЕЙ


class Studogochi(Game):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background_image = pygame.image.load('images/background.jpeg')
        self.screen.blit(self.background_image, (0, 0))
        self.clock = pygame.time.Clock()
        self.objects = []
        self.gamer = Student(500, 400, 100, 200, 'Bob', 'images/student.jpeg')
        self.button_health = Button(250, 575, 76, 50, 'images/images.png', characteristic='health')
        self.button_fatigue = Button(375, 575, 90, 50, 'images/fatigue.jpg', characteristic='fatigue')
        self.button_grades = GradesButton(460, 575, 59, 50, 'images/grades.png', characteristic='grades')
        self.button_money = Button(540, 575, 50, 50, 'images/money.jpg', characteristic='money')
        self.button_alcohol = Button(625, 575, 51, 75, 'images/bottle_new.jpg', characteristic='alcohol')
        self.statusbar_health = StatusHealth(250, 20, 50, 20, (220, 20, 60), WHITE,
                                             value=self.gamer.statistics['health'], surface=self.screen)
        self.statusbar_fatigue = StatusFatigue(325, 20, 50, 20, (0, 100, 0), WHITE,
                                               value=self.gamer.statistics['fatigue'], surface=self.screen)
        self.statusbar_grades = StatusGrades(400, 20, 50, 20, (0, 128, 128), WHITE,
                                             value=self.gamer.statistics['grades'], surface=self.screen)
        self.statusbar_money = StatusMoney(475, 20, 50, 20, (255, 140, 0), WHITE,
                                           value=self.gamer.statistics['money'], surface=self.screen)
        self.statusbar_alcohol = StatusAlcohol(550, 20, 50, 20, (0, 0, 102), WHITE,
                                               value=self.gamer.statistics['alcohol'], surface=self.screen)
        self.timer = Timer(70, 20, 60, 25, (255, 255, 255), (0, 0, 0), 0)  # ADDED
        self.clocks = Clocks(0, datetime.datetime.now())
        self.gameover = InfoGameover(250, 160, 300, 300, (255, 255, 255), (0, 0, 0), 0, self.gamer, self.clocks,
                                      self.screen)
        self.menu = Menu(0, 0, 800, 600, (0, 0, 0), (255, 255, 255, 0.5), self.screen, self.clocks)
        self.HEALTH_DECREASE = pygame.USEREVENT  # TODO сделать эти переменные через список
        self.FATIGUE_DECREASE = pygame.USEREVENT + 1
        self.MONEY_DECREASE = pygame.USEREVENT + 2
        self.ALCOHOL_DECREASE = pygame.USEREVENT + 3
        self.GRADES = pygame.USEREVENT + 4

    def draw_all(self):
        self.statusbar_health.draw(self.screen)

        self.statusbar_fatigue.draw(self.screen)
        self.statusbar_grades.draw(self.screen)
        self.statusbar_money.draw(self.screen)
        self.statusbar_alcohol.draw(self.screen)
        self.gamer.draw(self.screen)

        self.button_health.draw(self.screen)
        self.button_fatigue.draw(self.screen)
        self.button_grades.draw(self.screen)
        self.button_money.draw(self.screen)
        self.button_alcohol.draw(self.screen)

        self.timer.draw(self.screen)
        timer_value = self.timer.font.render(str(self.clocks.days) + '  days', True,
                                             self.timer.txt_color,
                                             self.timer.color)
        self.screen.blit(timer_value, (self.timer.bounds.x + 4, self.timer.bounds.y))

        pygame.display.update()

    def run(self):
        pygame.display.set_caption('Studogochi')
        run = True
        m_open = False
        pygame.time.set_timer(self.HEALTH_DECREASE, 5000)
        pygame.time.set_timer(self.FATIGUE_DECREASE, 5000)
        pygame.time.set_timer(self.MONEY_DECREASE, 10000)
        pygame.time.set_timer(self.ALCOHOL_DECREASE, 35000)
        pygame.time.set_timer(self.GRADES, 10000)

        self.gamer.subscribe('health', self.statusbar_health)  # TODO возможно не нужно каждый раз их подписывать
        self.gamer.subscribe('fatigue', self.statusbar_fatigue)
        self.gamer.subscribe('grades', self.statusbar_grades)  # Вынести названия статусбаров в список и подписывать их в цикле
        self.gamer.subscribe('money', self.statusbar_money)
        self.gamer.subscribe('alcohol', self.statusbar_alcohol)
        self.gamer.subscribe('gameover', self.gameover)

        while run:
            if self.gameover.game_end:
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()

                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
            elif m_open:
                self.menu.open_menu(self.background_image, m_open)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                        if event.key == pygame.K_F1:
                            m_open = False
                            self.menu.open_menu(self.background_image, m_open)
            else:
                #TIMER
                elapsedTime = datetime.datetime.now() - self.clocks.previous_time
                x = divmod(elapsedTime.total_seconds(), 60)
                if int(x[1]) < TIMER_DAYS:
                    pass
                else:
                    self.clocks.days += 1
                    self.clocks.previous_time = datetime.datetime.now()
                    self.draw_all()
                    self.clock.tick(60)
                self.draw_all()
                self.clock.tick(60)
                # pygame.time.delay(100) #я не знаю зачем нам нужна это строчка

                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()

                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                        if event.key == pygame.K_F1:
                            m_open = True
                            
                    # Уменьшаем значения
                    elif event.type == self.HEALTH_DECREASE:
                        self.gamer.update_statistic('health', -5)
                    elif event.type == self.FATIGUE_DECREASE:
                        self.gamer.update_statistic('fatigue', -8)
                    elif event.type == self.MONEY_DECREASE:
                        self.gamer.update_statistic('money', -7)
                    elif event.type == self.ALCOHOL_DECREASE:
                        self.gamer.update_statistic('alcohol', -6)
                    elif event.type == self.GRADES:
                        self.gamer.update_grades(0)

                    # Нажатие кнопок
                    elif (self.button_health.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('health', 10)
                        pygame.time.wait(1000)
                    elif (self.button_fatigue.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('fatigue', 10)
                        pygame.time.wait(1000)
                    elif (self.button_grades.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_grades(2)
                        pygame.time.wait(1000)
                    elif (self.button_money.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('money', 10)
                        pygame.time.wait(1000)
                    elif (self.button_alcohol.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('alcohol', 10)
                        pygame.time.wait(1000)






