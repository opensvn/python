from random import *
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()    
            pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))

    pygame.display.update()