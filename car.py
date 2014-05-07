import pygame
import random
from constants import *
from highway import *

class CarImage(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill(CARCOLOR)
        self.updatePosition(x, y)

    def updatePosition(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changeColor(self, color):
        self.color = color
        self.image.fill(color)

class Car():
    def __init__(self, cid, (x, y)):
        self.cid = cid
        self.sprite = pygame.sprite.RenderPlain()
        self.currentHighway = 0
        self.x = x
        self.y = y + 2
        self.dx = 0.1 + random.random() * (CARSPEED - 0.1)
        self.dy = 0
        self.car = CarImage(self.x, self.y, CARWIDTH, CARHEIGHT)
        self.sprite.add(self.car)
        self.decbuffer = CarImage(self.x + CARWIDTH + 2, self.y, SPACING * self.dx, CARHEIGHT)
        self.incbuffer = CarImage(self.x + CARWIDTH + 2, self.y, SPACING * self.dx * 4, CARHEIGHT)
        self.isSelected = False
        #self.bbuffer = 

    def setPosition(self, (x, y)):
        self.x = x
        self.y = y + 2 #offset inside highway
        for s in self.sprite:
            s.updatePosition(self.x, self.y)
        self.decbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)
        self.incbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)

    def collide(self, p):
        return self.car.rect.collidepoint(p)

    def slowDown(self):
        self.dx = max(self.dx * 0.9, 0.1)
        self.decbuffer.image = pygame.Surface([SPACING * self.dx, CARHEIGHT])
        self.incbuffer.image = pygame.Surface([SPACING * self.dx * 3, CARHEIGHT])

    def speedUp(self):
        self.dx = min(self.dx * 1.1, 0.5)
        self.decbuffer.image = pygame.Surface([SPACING * self.dx, CARHEIGHT])
        self.incbuffer.image = pygame.Surface([SPACING * self.dx * 3, CARHEIGHT])

    def updatePosition(self, allcars):
        if pygame.sprite.spritecollideany(self.decbuffer, allcars) is not None and not self.isSelected:
            self.slowDown()
        if pygame.sprite.spritecollideany(self.incbuffer, allcars) is None and not self.isSelected:
            self.speedUp()

        self.x += self.dx
        if self.x + CARSIZE >= HEND:
            return True 
        else:
            self.y += self.dy
            for s in self.sprite:
                s.updatePosition(self.x, self.y)
            self.decbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)
            self.incbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)
        return False

    def getCurrentHighway(self):
        return self.currentHighway

    def setHighway(self, hid, highway):
        self.currentHighway = hid
        #TODO: more

    def selected(self, s):
        if s:
          self.car.changeColor(red)
        else:
          self.car.changeColor(CARCOLOR)
        self.isSelected = s



