import pygame
from pygame.sprite import Sprite
from player import Player


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.img = pygame.image.load('images/python.png')
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.direction = True;
        

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        if self.direction == True:
            self.rect.midright = ai_game.player.rect.midright
        else:
             self.rect.midleft = ai_game.player.rect.midleft

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.x)

    def update(self):
        print(self.direction)
        self.bullet_Direction(self.direction);
        if self.direction == False:
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

    def bullet_Direction(self, direction):
        return direction;

