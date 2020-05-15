import pygame
from button import *
from abc import ABC
from statusbar import *
from student import Student
from game import Game
import datetime
import time
from menu import *
from random_events import *

WHITE = (255, 255, 255)
TIMER_DAYS = 5  # ЭТО ОТВЕЧАЕТ ЗА БЫСТРОТУ ПРОТЕКАНИЯ ДНЕЙ
SIZE_OF_WINDOW = (640, 660)


class Studogochi(Game):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_OF_WINDOW)
        self.background_image = pygame.image.load('images/backgrounds/main_background.png')
        self.buttons_background = pygame.image.load('images/backgrounds/buttons_back.png')
        self.clock = pygame.time.Clock()
        self.objects = []
        self.gamer = Student(x=620, y=542, width=270, height=420, name='Bob', image='images/student_female.png',
                             surface=self.screen)

        self.button_health = Button(x=257, y=646, width=90, height=90, image='images/buttons/eat_button.png',
                                    characteristic='health', surface=self.screen)
        self.button_fatigue = Button(x=582, y=646, width=90, height=90, image='images/buttons/sleep_button.png',
                                     characteristic='fatigue', surface=self.screen)
        self.button_grades = GradesButton(x=365, y=646, width=90, height=90, image='images/buttons/study_button.png',
                                          characteristic='grades', surface=self.screen)
        self.button_money = Button(x=473, y=646, width=90, height=90, image='images/buttons/money_button.png',
                                   characteristic='money', surface=self.screen)
        self.button_alcohol = Button(x=149, y=646, width=90, height=90, image='images/buttons/drink_button.png',
                                     characteristic='alcohol', surface=self.screen)
        self.statusbar_health = StatusAlcohol(x=350, y=150, width=290, height=65, txt_color=WHITE,
                                              value=self.gamer.statistics['health'], surface=self.screen,
                                              background='images/backgrounds/health_back.png',
                                              characteristic='health')
        self.statusbar_fatigue = StatusFatigue(x=640, y=150, width=290, height=65, txt_color=WHITE,
                                               value=self.gamer.statistics['fatigue'], surface=self.screen,
                                               background='images/backgrounds/fatigue_back.png',
                                               characteristic='fatigue')
        self.statusbar_grades = StatusGrades(x=350, y=225, width=290, height=65, txt_color=WHITE,
                                             value=self.gamer.statistics['grades'], surface=self.screen,
                                             background='images/backgrounds/grades_back.png',
                                             characteristic='grades')
        self.statusbar_money = StatusMoney(x=640, y=75, width=290, height=65, txt_color=WHITE,
                                           value=self.gamer.statistics['money'], surface=self.screen,
                                           background='images/backgrounds/money_back.png',
                                           characteristic='money')
        self.statusbar_alcohol = StatusAlcohol(x=350, y=75, width=290, height=65, txt_color=WHITE,
                                               value=self.gamer.statistics['alcohol'], surface=self.screen,
                                               background='images/backgrounds/alcohol_back.png',
                                               characteristic='alcohol')
        self.timer = Timer(x=270, y=400, width=120, height=90, surface=self.screen,
                           txt_color=(0, 0, 0), value=0, background='images/calendar.png')  # ADDED
        self.clocks = Clocks(0, datetime.datetime.now())
        self.gameover = InfoGameover(x=250, y=160, width=550, height=550,
                                     color=(255, 255, 255), txt_color=(0, 0, 0), value=0, gamer=self.gamer,
                                     clocks=self.clocks, screen=self.screen, size_of_window=SIZE_OF_WINDOW)
        self.menu = Menu(x=0, y=0, width=SIZE_OF_WINDOW[0], height=SIZE_OF_WINDOW[1], text_color=(25, 25, 25),
                         color=(243, 243, 243, 140), screen=self.screen, clocks=self.clocks)
        self.health_event = RandomEventHealth(x=250, y=160, width=550, height=550, screen=self.screen,
                                              days = self.clocks, gamer = self.gamer, size_of_window = SIZE_OF_WINDOW)
        self.HEALTH_DECREASE = pygame.USEREVENT  # TODO сделать эти переменные через список
        self.FATIGUE_DECREASE = pygame.USEREVENT + 1
        self.MONEY_DECREASE = pygame.USEREVENT + 2
        self.ALCOHOL_DECREASE = pygame.USEREVENT + 3
        self.GRADES = pygame.USEREVENT + 4

    def draw_all(self):
        self.screen.blit(self.background_image, (-300, 0))
        self.screen.blit(self.buttons_background, (40, 542))

        self.statusbar_health.draw()
        self.statusbar_fatigue.draw()
        self.statusbar_grades.draw()
        self.statusbar_money.draw()
        self.statusbar_alcohol.draw()
        self.gamer.draw()

        self.button_health.draw()
        self.button_fatigue.draw()
        self.button_grades.draw()
        self.button_money.draw()
        self.button_alcohol.draw()

        timer_value = self.timer.font.render(str(self.clocks.days), True,
                                             self.timer.txt_color)
        self.timer.draw(timer_value, self.clocks.days)
        pygame.display.update()

    def run(self):
        pygame.display.set_caption('Studogochi')
        run = True
        m_open = False
        pygame.time.set_timer(self.HEALTH_DECREASE, 5000)
        pygame.time.set_timer(self.FATIGUE_DECREASE, 5000)  # 5000
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
                        if event.key == pygame.K_r:
                            self.gameover.restart()
                            self.draw_all()
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
                # TIMER
                elapsedTime = datetime.datetime.now() - self.clocks.previous_time
                x = divmod(elapsedTime.total_seconds(), 60)
                if int(x[1]) < TIMER_DAYS:
                    pass
                else:
                    self.clocks.days += 1
                    self.clocks.previous_time = datetime.datetime.now()
                    self.draw_all()
                    self.clock.tick(60)
                    self.health_event.random_event()
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
                    elif (self.button_fatigue.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('fatigue', 10)
                    elif (self.button_grades.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_grades(2)
                    elif (self.button_money.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('money', 10)
                    elif (self.button_alcohol.push(pos[0], pos[1], click[0], self.screen) is True):
                        self.gamer.update_statistic('alcohol', 10)
