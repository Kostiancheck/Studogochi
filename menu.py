import pygame
from game_object import GameObject
from exception import *
from interface_draw import IDraw


class Menu(GameObject, IDraw):
    def __init__(self, x, y, width, height, text_color, color, screen, clocks):
        super().__init__(x, y, width, height)
        self.font = pygame.font.Font('fonts/Raleway-Light.ttf', 15)
        self.text_color = text_color
        self.color = color
        self.open = False
        self.screen = screen
        self.clocks = clocks

    def draw(self, surface):
        surface.fill(self.color)
        #pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def open_menu(self, background_image, trigger):
        if trigger:
            self.draw(self.screen)
            self.screen.blit(pygame.font.Font('fonts/Montserrat-Thin.ttf', 45).render(
                    'MENU', True, self.text_color), ((self.width/2)-70, 20))
            pygame.draw.rect(self.screen, (25,25,25), (40, 80, self.width - 80, 1))
            data = list()
            data.append(["F1", "Show/Close Help"])
            data.append(["Esc", "Exit Game"])
            data.append(["R", "Restart Game  (Only if you lose)"])
            data.append(['You alived: ', str(self.clocks.days) + ' days in our wonderful university :)'])
            for i, text in enumerate(data):
                self.screen.blit(self.font.render(
                    text[0], True, self.text_color), (100, 100 + 35 * i))
                self.screen.blit(self.font.render(
                    text[1], True, self.text_color), (200, 100 + 35 * i))
            pygame.display.update()
        else:
            self.screen.blit(background_image, (0, 0))
           


class InfoGameover(GameObject, IDraw):
    def __init__(self, x, y, width, height, color, txt_color, value, gamer, clocks, screen, size_of_window, surface=None):
        super().__init__(x, y, width, height)
        self.color = color
        self.value = value
        self.txt_color = txt_color
        self.surface = surface
        self.font = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 30)
        self.image = 'images/game_over.jpg'
        self.game_end = False
        self.gamer = gamer
        self.clocks = clocks
        self.screen = screen
        self.size_of_window = size_of_window

    def draw(self, surface):
        surf = pygame.image.load('images/backgrounds/gameover_back.png')
        surf = pygame.transform.scale(surf, (self.width, self.height))
        a = (self.size_of_window[0]-self.width)/2
        b = (self.size_of_window[1]-self.height)/2
        rect = surf.get_rect(bottomright=(self.width+a, self.height+b))
        surface.blit(surf, rect)
        return (a, b)
        #pygame.draw.rect(surface, self.color, (self.bounds.x, self.bounds.y, self.bounds.width, self.bounds.height))

    def update_status(self, char, num):
        self.is_end(char, num)

    def restart(self):
        self.game_end = False
        self.gamer.statistics['health'] = 100
        self.gamer.statistics['fatigue'] = 100
        self.gamer.statistics['grades'] = 0
        self.gamer.statistics['money'] = 1000
        self.gamer.statistics['alcohol'] = 10
        for i in self.gamer.statistics.keys():
            self.gamer.update_statistic(i, 0, self.screen)
        self.gamer.update_grades(0)
        self.clocks.days = 0

    def is_end(self, stat, num):
        try:
            if stat == 'grades':
                if int(num) < 60 and int(self.clocks.days) >= 365:
                    raise NegativeStatisticGrades(stat)

            elif int(num) <= 0:
                raise NegativeStatistic(stat)

        except NegativeStatisticGrades as n:
            sizes = self.draw(self.screen)
            font_1 = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 50)
            game_over_str = font_1.render("Game over", True,
                                             self.txt_color,
                                             self.color)
            game_over_str.set_colorkey(self.color)
            self.screen.blit(game_over_str, (sizes[0]+(self.width/2)-110, sizes[1]+20))
            surf = pygame.image.load('images/coffin.png')
            a = (self.width-147)/2
            b = (self.height-252)/2
            rect = surf.get_rect(bottomright=(a+200,b+252))
            self.screen.blit(surf, rect)
            game_over_why = self.font.render("You are in the army now", True,
                                             self.txt_color,
                                             self.color)
            game_over_why.set_colorkey(self.color)
            self.screen.blit(game_over_why, (sizes[0]+(self.width/2)-170, sizes[1]+400))
            game_over_exit = self.font.render("Presss Esc to exit R to restart", True,
                                              self.txt_color,
                                              self.color)
            game_over_exit.set_colorkey(self.color)
            self.screen.blit(game_over_exit, (sizes[0]+(self.width/2)-190, sizes[1]+450))
            self.game_end = True
            pygame.display.update()

        except NegativeStatistic as m:
            sizes = self.draw(self.screen)
            font_1 = pygame.font.Font('fonts/Indie_Flower/IndieFlower.ttf', 50)
            game_over_str = font_1.render("Game over", True,
                                             self.txt_color,
                                             self.color)
            game_over_str.set_colorkey(self.color)
            self.screen.blit(game_over_str, (sizes[0]+(self.width/2)-110, sizes[1]+20))
            surf = pygame.image.load('images/coffin.png')
            a = (self.width-147)/2
            b = (self.height-252)/2
            rect = surf.get_rect(bottomright=(a+200,b+252))
            self.screen.blit(surf, rect)
            game_over_why = self.font.render("You lose because of {}".format(m), True,
                                             self.txt_color,
                                             self.color)
            game_over_why.set_colorkey(self.color)
            self.screen.blit(game_over_why, (sizes[0]+(self.width/2)-170, sizes[1]+400))
            game_over_exit = self.font.render("Presss Esc to exit R to restart", True,
                                              self.txt_color,
                                              self.color)
            game_over_exit.set_colorkey(self.color)
            self.screen.blit(game_over_exit, (sizes[0]+(self.width/2)-190, sizes[1]+450))
            self.game_end = True
            pygame.display.update()
