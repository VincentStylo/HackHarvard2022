from re import S
import sys
from time import sleep
from turtle import left
from player import Player
from obstacle import *
from enemy import *

import pygame

from bullet import *
from settings import Settings

right_direction = True;


class HackHeartvard:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.img = "images/bg1.png"
        image = pygame.image.load("images/menu.png")
        image = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image, (0, 0))
        pygame.display.set_caption("Hack Heartvard")

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()

        self.obstacle = Obstacle(self)
        self.obstacle2 = Obstacle2(self)

        self.enemy1 = Enemy1(self)
        self.enemy2 = Enemy2(self)

    def run_game(self):
        self.image = pygame.image.load(self.img)
        self.image = pygame.transform.scale(self.image, (800, 600))
        while True:
            self.screen.blit(self.image, (0, 0))
            self._check_events()
            self._update_screen()
            self._update_background()
            self.player.update()
            self._update_bullets()
            self.player.collision()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_d:
            self.player.moving_right = True
            self.right_Direction = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
            self.right_Direction = False
        elif event.key == pygame.K_w:
            self.player.jump = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        if event.key == pygame.K_a:
            self.player.moving_left = False
        if event.key == pygame.K_w:
            self.player.jump = False

    def _update_screen(self):
        self.player.blitme()
        self.obstacle.blitme()
        self.obstacle2.blitme()
        self.enemy1.blitme()
        self.enemy2.blitme()
        pygame.display.flip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _update_background(self):
        image = pygame.image.load(self.img)
        image = pygame.transform.scale(image, (800, 600))
        pygame.display.flip()
        return image

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            new_bullet.bullet_Direction(right_direction)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 900:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # Creates the game, and runs it
    ai = HackHeartvard()
    ai.run_game()
