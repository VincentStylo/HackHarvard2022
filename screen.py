import pygame
from level import *

pygame.init()


def Menu():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hack Heartvard")
    image = pygame.image.load("images/menu.png")
    image = pygame.transform.scale(image, (800, 600))
    while True:
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    Level()
