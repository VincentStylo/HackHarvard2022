import pygame
from pygame.sprite import Sprite
from bullet import Bullet


class Enemy1(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the player image and gets its rect.
        self.image = pygame.image.load("images/enemy1.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        self.rect.midright = self.screen_rect.midright
        self.rect.y -= 75

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def collision(self):
        return self.rect.colliderect(Bullet(self).collisionBox())


class Enemy2(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the player image and gets its rect.
        self.image = pygame.image.load("images/enemy2.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen_rect.bottomright
        self.rect.y -= 75

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def collision(self):
        return self.rect.colliderect(Bullet(self).collisionBox())