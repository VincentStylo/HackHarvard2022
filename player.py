import pygame


def loadPlayer():
    image = pygame.image.load("images/player.png")
    image = pygame.transform.scale(image, (50, 50))
    return image


def displayPlayer(screen, image):
    screen.blit(image, (50, 400))
    pygame.display.update()
