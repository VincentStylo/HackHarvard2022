import pygame
from time import sleep

from pygame.sprite import Sprite
from obstacle import Obstacle


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

        # Start each new ship at the bottom center of the screen.
        self.rect.bottomleft = self.screen_rect.bottomleft

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.jump = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the playrs x value, not the rect.
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
        elif not self.jump and self.y < self.screen_rect.bottom - 75:
            if (self.collision()):
                self.y = Obstacle(self).collisionBox().top - 75
            else:
                self.jump = False
                self.y += 10

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def collision(self):
        return self.rect.colliderect(Obstacle(self).collisionBox())
