import pygame
import pickle

from world import *
from highway import *
from car import *
from constants import *
import time

def newSim():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Blah")
    world = World()
    mainLoop(screen, world)

def drawText(screen, message, x, y, size):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, black, white)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    screen.blit(text, textRect)

def mainLoop(screen, world):
    print "alkjsldjf"
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(white)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    world.addCar()
        # update everything
        world.update()

        # redraw everything
        screen.blit(background, (0, 0))
        world.redraw(screen)
        for car in world.cars:
            car.sprite.draw(screen)
        pygame.display.flip()

    #world.redraw()
    #pygame.display.flip()

newSim()

