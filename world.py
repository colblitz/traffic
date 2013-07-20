import pygame
from pygame.locals import *
from constants import *
from highway import *
from car import *

class World:
    def __init__(self):
        self.highways = []
        self.cars = []
        self.carsOnHighway = {}
        self.addHighways()
        self.nextcar = 0
        self.allCarSprites = pygame.sprite.RenderPlain()

    def addHighways(self):
        for i in xrange(HIGHWAYS):
            highway = Highway(HSTART, HEND, HOFFSET + i * (HWIDTH + HSPACE), LANES, i)
            self.highways.append(highway)
            self.carsOnHighway[i] = []

    def addCar(self):
        car = Car(self.nextcar, self.highways[0].getStart())
        self.nextcar += 1
        self.cars.append(car)
        self.carsOnHighway[0].append(car.cid)
        self.allCarSprites.add(car.sprite)

    #TODO: remove car? no need yet

    def updateCars(self):
        for car in self.cars:
            if car.updatePosition(self.allCarSprites):
                # move to next highway
                car.currentHighway += 1
                if car.currentHighway == HIGHWAYS:
                    car.currentHighway = 0
                car.setPosition(self.highways[car.currentHighway].getStart())

    def moveToNext(self, carID):
        hid = self.cars[carID].currentHighway()
        self.carsOnHighway[hid].remove(carID)
        if hid == HIGHWAYS - 1:
            hid = 0
        else:
            hid = hid + 1
        self.cars[carID].setHighway(hid, self.highways[hid].getStart())
        self.carsOnHighway[hid].append(carID)

    def update(self):
        self.updateCars()

    def redraw(self, screen):
        for highway in self.highways:
            highway.draw(screen)
        #for car in self.cars:
        #    car.sprite.draw(screen)


