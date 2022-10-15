import pygame
from screen import *
from player import *
from movement import *
from time import sleep


def level():
    image = pygame.image.load("images/menu.png")
    image = pygame.transform.scale(image, (800, 600))
    screen = pygame.display.set_mode((800, 600))
    image2 = loadPlayer()
    x = 0
    y = 0
    while True:
        screen.blit(image, (0, 0))
        x = Move(x)
        y = Jump(y)
        displayPlayer(screen, image2, x, y)
        pygame.display.update()
        y = 0
        pygame.display.update()
