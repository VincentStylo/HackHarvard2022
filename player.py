import pygame
from time import sleep


def loadPlayer():
    image = pygame.image.load("images/player.png")
    image = pygame.transform.scale(image, (50, 50))
    return image


def displayPlayer(screen, image, x, y):
    screen.blit(image, (50 + x, 400 + y))
    pygame.display.update()
