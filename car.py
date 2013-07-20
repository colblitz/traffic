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

class Car():
    def __init__(self, cid, (x, y)):
        self.cid = cid
        self.sprite = pygame.sprite.RenderPlain()
        self.currentHighway = 0
        self.x = x
        self.y = y + 2
        self.dx = 0.1 + random.random() * (CARSPEED - 0.1)
        self.dy = 0
        self.sprite.add(CarImage(self.x, self.y, CARWIDTH, CARHEIGHT))
        self.decbuffer = CarImage(self.x + CARWIDTH + 2, self.y, SPACING * self.dx, CARHEIGHT)
        self.incbuffer = CarImage(self.x + CARWIDTH + 2, self.y, SPACING * self.dx * 4, CARHEIGHT)
        #self.bbuffer = 

    def setPosition(self, (x, y)):
        self.x = x
        self.y = y + 2 #offset inside highway
        for s in self.sprite:
            s.updatePosition(self.x, self.y)
        self.decbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)
        self.incbuffer.updatePosition(self.x + CARWIDTH + 2, self.y)

    def updatePosition(self, allcars):
        if pygame.sprite.spritecollideany(self.decbuffer, allcars) is not None:
            print "collision, reducing!"
            self.dx = max(self.dx * 0.9, 0.1)
            self.decbuffer.image = pygame.Surface([SPACING * self.dx, CARHEIGHT])
            self.incbuffer.image = pygame.Surface([SPACING * self.dx * 3, CARHEIGHT])
        if pygame.sprite.spritecollideany(self.incbuffer, allcars) is None:
            print "no cars, speed up!"
            self.dx = min(self.dx * 1.1, 0.5)
            self.decbuffer.image = pygame.Surface([SPACING * self.dx, CARHEIGHT])
            self.incbuffer.image = pygame.Surface([SPACING * self.dx * 3, CARHEIGHT])
        #self.oldx = self.x
        #for s in self.sprite:
        #    s.updatePosition(self.x + SPACING*self.dx)

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



