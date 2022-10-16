import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/obstacle.png")
        self.image = pygame.transform.scale(self.image, (250, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen_rect.bottomright
        self.rect.y -= 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def collisionBox(self):
        return self.rect


class Obstacle2(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/obstacle.png")
        self.image = pygame.transform.scale(self.image, (250, 75))
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright
        self.rect.y -= 100

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def collisionBox(self):
        return self.rect
