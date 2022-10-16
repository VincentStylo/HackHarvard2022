from re import S
import sys
from time import sleep
from turtle import left
from player import Player
from obstacle import *
from enemy import *
from cutscene import *
from button import *

import pygame

from bullet import *
from settings import Settings


class zakHarvard:
    def __init__(self):
        pygame.init()
        mixer.init()
        mixer.music.load('music/Ultra.wav')
        mixer.music.play(-1)
        self.intro = Intro(self)
        mixer.music.load('music/AllStar.wav')
        mixer.music.play(-1)

        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.img = "images/bg.png"
        image = pygame.image.load("images/menu.png")
        image = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image, (0, 0))
        pygame.display.set_caption("Zak Harvard")
        self.right_Direction = False
        self.count = 0

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemyBullets = pygame.sprite.Group()

        self.obstacle = Obstacle(self)
        self.obstacle2 = Obstacle2(self)

        self.enemy1 = Enemy1(self)
        self.enemy2 = Enemy2(self)
        self.boss = Boss(self)

        self.gameStatus = False
        self.bossStatus = False
        self.hasPlayed = False

        self.play_button = Button(self, "Play")

    def run_game(self):
        i = 0
        self.image = pygame.image.load(self.img)
        self.image = pygame.transform.scale(self.image, (800, 600))
        while True:
            i += 1
            self.screen.blit(self.image, (0, 0))
            self._check_events()
            if (i % 100 == 0):
                self._fire_Ebullet()
                if (i > 100):
                    i = 0
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
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
        if event.key == pygame.K_d:
            self.player.moving_right = False
        if event.key == pygame.K_a:
            self.player.moving_left = False
        if event.key == pygame.K_w:
            self.player.jump = False

    def _update_screen(self):
        if not self.gameStatus:
            self.play_button.draw_button()
        if self.enemy1.lives <= 0 and self.enemy2.lives <= 0:
            self.bossStatus = True
        self.player.blitme()
        if not self.bossStatus:
            self.enemy1.blitme()
            self.obstacle.blitme()
            self.enemy2.blitme()
            self.obstacle2.blitme()
        elif self.bossStatus and self.boss.lives > 0:
            self.boss.blitme()
            if not self.hasPlayed:
                self.playBossScene()
        if self.boss.lives <= 0:
            self.playEnding()

        pygame.display.flip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.enemyBullets.sprites():
            bullet.draw_bullet()

    def _update_background(self):
        image = pygame.image.load(self.img)
        image = pygame.transform.scale(image, (800, 600))
        pygame.display.flip()
        return image

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            new_bullet.bullet_Direction(self.right_Direction)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 900 or bullet.rect.left <= 0:
                self.bullets.remove(bullet)
            if bullet.rect.x - self.enemy1.rect.x <= 5 and bullet.rect.y - self.enemy1.rect.y <= 5 and self.enemy1.lives > 0:
                self.enemy1.lives -= 1
                print(self.enemy1.lives)
                self.bullets.remove(bullet)
            if bullet.rect.x - self.enemy2.rect.x <= 5 and bullet.rect.y - self.enemy2.rect.y <= 5 and self.enemy2.lives > 0:
                self.enemy2.lives -= 1
                print(self.enemy2.lives)
                self.bullets.remove(bullet)
            if bullet.rect.x - self.boss.rect.x <= 5 and bullet.rect.y - self.boss.rect.y <= 5 and self.boss.lives > 0 and self.bossStatus:
                self.boss.lives -= 1
                print(self.boss.lives)
                self.bullets.remove(bullet)

    def _fire_Ebullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            if (self.enemy1.lives > 0):
                new_bullet = Enemy1Bullet(self)
                new_bullet.bullet_Direction(self.right_Direction)
                self.bullets.add(new_bullet)
            if (self.enemy2.lives > 0):
                new_bullet2 = Enemy2Bullet(self)
                new_bullet2.bullet_Direction(self.right_Direction)
                self.bullets.add(new_bullet2)
            if (self.enemy2.lives == 0 and self.enemy1.lives == 0):
                self.bossStatus = True
                new_bullet3 = BossBullet(self)
                new_bullet3.bullet_Direction(self.right_Direction)
                self.bullets.add(new_bullet3)

    def _update_Ebullets(self):
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 900 or bullet.rect.left <= 0:
                self.bullets.remove(bullet)
            if bullet.rect.x - self.player.rect.x <= 5 and bullet.rect.y - self.player.rect.y == 5:
                self.bullets.remove(bullet)
                self.player.lives -= 1
                if (self.player.lives == 0):
                    sys.exit()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if (button_clicked):
            self.gameStatus = True

    def playBossScene(self):
        self.end = End(self)
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.hasPlayed = True

    def playEnding(self):
        self.final = Final(self)
        pygame.quit()


if __name__ == '__main__':
    # Creates the game, and runs it
    ai = zakHarvard()
    ai.run_game()
