#coded by - SUYASH MADALE
import pygame
#PADDLE
class Player(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xx = self.x + self.w
        self.yy = self.y + self.h

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])

    def move(self,sw,sh):
        if pygame.mouse.get_pos()[0] - self.w//2 < 0:
            self.x = 0
        elif pygame.mouse.get_pos()[0] + self.w//2 > sw:
            self.x = sw - self.w
        else:
            self.x = pygame.mouse.get_pos()[0] - self.w //2


class Ball(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xv = 5
        self.yv = 5
        self.xx = self.x + self.w
        self.yy = self.y + self.h

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])
    #MOVEMENT
    def move(self,sw,sh):
        self.x += self.xv
        self.y += self.yv
        if self.x + self.w> sw or self.x<0:
            self.xv *= -1
        elif self.y <= 0:
            self.yv *= -1

class Brick(object):
    def __init__(self, x, y, w, h,strength,score):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = True
        self.xx = self.x + self.w
        self.yy = self.y + self.h
        self.strength=strength
        self.score=score
        self.color=(0,0,0)


    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])
    def color_assign(self):
        if self.strength==1:
            self.color=(128,0,191)
        elif self.strength==2:
            self.color=(61,0,191)
        elif self.strength==3:
            self.color=(76,255,0)
        elif self.strength==4:
            self.color=(255,255,0)
        elif self.strength==5:
            self.color=(255,127,0)
        elif self.strength==6:
            self.color=(255,0,0)