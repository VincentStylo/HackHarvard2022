from pickle import TRUE
import pygame
from time import sleep
from bullet import *

from pygame.sprite import Sprite
from obstacle import *


class Player(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the player image and gets its rect.
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        # Start each new player at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the player's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.jump = False
        self.lives = 5

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.collision():
                self.x -= 5.5
            else:
                self.x += 5.5
        if self.moving_left and self.rect.left > 0:
            if self.collision():
                self.x += 5.5
            else:
                self.x -= 5.5
        if self.x > self.screen_rect.right - 100:
            self.x = 0
        if self.jump and self.y > 0:
            if self.collision():
                self.y += 10
            else:
                self.y -= 10
        elif not self.jump and self.y < self.screen_rect.bottom - 200:
            if (self.collision()):
                self.y = Obstacle(self).collisionBox().top - 75
            else:
                self.jump = False
                self.y += 10

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def collision(self):
        if (self.rect.colliderect(Obstacle(self).collisionBox()) or self.rect.colliderect(Obstacle2(self).collisionBox())):
            return True

    def collisionBox(self):
        return self.rect
