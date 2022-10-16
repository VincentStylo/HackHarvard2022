import pygame
from pygame.sprite import Sprite
from enemy import Enemy1, Enemy2


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.img = pygame.image.load('images/python.png')
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.direction = True

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = ai_game.player.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        newDirection = self.bullet_Direction(self.direction)
        if newDirection == False:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x -= self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x
        else:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x += self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.img, self.rect)

    def bullet_Direction(self, newDirection):
        return newDirection

    def collisionBox(self):
        return self.rect


class Enemy1Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.img = pygame.image.load('images/python.png')
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.direction = True

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(100, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        if self.direction == False:
            self.rect.midright = ai_game.enemy1.rect.midright
        else:
            self.rect.midleft = ai_game.enemy1.rect.midleft

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = 100
        newDirection = self.bullet_Direction(self.direction)
        if newDirection == True:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x -= self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x
        else:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x += self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.img, self.rect)

    def bullet_Direction(self, newDirection):
        return newDirection

    def collisionBox(self):
        return self.rect


class Enemy2Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.img = pygame.image.load('images/python.png')
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.direction = True

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(100, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        if self.direction == False:
            self.rect.midright = ai_game.enemy2.rect.midright
        else:
            self.rect.midleft = ai_game.enemy2.rect.midleft

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = 100
        newDirection = self.bullet_Direction(self.direction)
        if newDirection == True:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x -= self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x
        else:
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.x += self.settings.bullet_speed
            # Update the rect position.
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.img, self.rect)

    def bullet_Direction(self, newDirection):
        return newDirection

    def collisionBox(self, item):
        return self.rect
