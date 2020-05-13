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
        self.screen = pygame.display.set_mode((720, 640))
        self.background_image = pygame.image.load('images/backgrounds/main_background.png')
        self.clock = pygame.time.Clock()
        self.objects = []
        self.gamer = Student(x=600, y=500, width=290, height=450, name='Bob', image='images/student_male.png')
        self.button_health = Button(x=250, y=575, width=95, height=95, image='images/buttons/eat_button.png', characteristic='health')
        self.button_fatigue = Button(x=350, y=575, width=95, height=95, image='images/buttons/sleep_button.png', characteristic='fatigue')
        self.button_grades = GradesButton(x=450, y=575, width=95, height=95, image='images/buttons/study_button.png', characteristic='grades')
        self.button_money = Button(x=550, y=575, width=95, height=95, image='images/buttons/money_button.png', characteristic='money')
        self.button_alcohol = Button(x=650, y=575, width=95, height=95, image='images/buttons/drink_button.png', characteristic='alcohol')
        self.statusbar_health = StatusHealth(x=250, y=20, width=50, height=20, color=(220, 20, 60), txt_color=WHITE,
                                             value=self.gamer.statistics['health'], surface=self.screen)
        self.statusbar_fatigue = StatusFatigue(x=325, y=20, width=50, height=20, color=(0, 100, 0), txt_color=WHITE,
                                               value=self.gamer.statistics['fatigue'], surface=self.screen)
        self.statusbar_grades = StatusGrades(x=400, y=20, width=50, height=20,color=(0, 128, 128), txt_color=WHITE,
                                             value=self.gamer.statistics['grades'], surface=self.screen)
        self.statusbar_money = StatusMoney(x=475, y=20, width=50, height=20, color=(255, 140, 0), txt_color=WHITE,
                                           value=self.gamer.statistics['money'], surface=self.screen)
        self.statusbar_alcohol = StatusAlcohol(x=550, y=20, width=50, height=20, color=(0, 0, 102), txt_color=WHITE,
                                               value=self.gamer.statistics['alcohol'], surface=self.screen)
        self.timer = Timer(x = 270, y = 270, width = 120, height = 90, color = (255, 255, 255), 
                            txt_color = (0, 0, 0), value = 0, backgound = 'images/calendar.png')  # ADDED
        self.clocks = Clocks(0, datetime.datetime.now())
        self.gameover = InfoGameover(250, 160, 300, 300, (255, 255, 255), (0, 0, 0), 0, self.gamer, self.clocks,
                                     self.screen)
        self.menu = Menu(x=0, y=0, width=720, height=640, text_color=(25, 25, 25),
                         color=(243,243,243,140), screen=self.screen, clocks=self.clocks)
        self.HEALTH_DECREASE = pygame.USEREVENT  # TODO сделать эти переменные через список
        self.FATIGUE_DECREASE = pygame.USEREVENT + 1
        self.MONEY_DECREASE = pygame.USEREVENT + 2
        self.ALCOHOL_DECREASE = pygame.USEREVENT + 3
        self.GRADES = pygame.USEREVENT + 4

    def draw_all(self):
        self.screen.blit(self.background_image, (-250, 0))

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

        timer_value = self.timer.font.render(str(self.clocks.days), True,
                                             self.timer.txt_color,
                                             self.timer.color)
        self.timer.draw(self.screen, timer_value)

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
        self.gamer.subscribe('grades',
                             self.statusbar_grades)  # Вынести названия статусбаров в список и подписывать их в цикле
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
