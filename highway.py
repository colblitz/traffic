import pygame
from pygame.locals import *
from constants import *

class Highway:
    def __init__(self, x1, x2, y, lanes, hid):
        ## TODO: check bounds (if x > WIDTH/2 or something)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y
        self.y2 = y + lanes * LANEWIDTH
        self.lanes = lanes
        self.hid = hid

    def getStart(self):
        return (self.x1, self.y1)

    def draw(self, screen):
        pygame.draw.line(screen, black, (self.x1, self.y1), (self.x1, self.y2))
        pygame.draw.line(screen, black, (self.x2, self.y1), (self.x2, self.y2))
        pygame.draw.line(screen, black, (self.x1, self.y2), (self.x2, self.y2))
        for i in xrange(self.lanes):
            pygame.draw.line(screen, black, (self.x1, self.y1 + i * LANEWIDTH), (self.x2, self.y1 + i * LANEWIDTH))

    def isIn(self, x, y):
        return x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2

    def whichLane(self, x, y):
        if self.isIn(x, y):
            return (y - self.y1) / LANEWIDTH
        else:
            return -1
