import pygame
from screen import *
from player import *


def level():
    image = pygame.image.load("images/menu.png")
    image = pygame.transform.scale(image, (800, 600))
    screen = pygame.display.set_mode((800, 600))
    image2 = loadPlayer()
    while True:
        screen.blit(image, (0, 0))
        displayPlayer(screen, image2)
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
                    print("Space")
