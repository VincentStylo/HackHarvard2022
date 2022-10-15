import sys
from time import sleep
from player import Player

import pygame

from bullet import Bullet
from settings import Settings



class HackHeartvard:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        image = pygame.image.load("images/menu.png")
        image = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image, (0, 0))
        pygame.display.set_caption("Hack Heartvard")

        self.player = Player(self)

    def run_game(self):
        while True:
            image = pygame.image.load("images/menu.png")
            image = pygame.transform.scale(image, (800, 600))
            self.screen.blit(image, (0, 0))
            self._check_events()
            self._update_background()
            self.player.update()
            self._update_screen()

    def _check_events(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False            

    def _update_screen(self):
        pygame.display.update()
        self.player.blitme()

    def _update_background(self):
        image = pygame.image.load("images/menu.png")
        image = pygame.transform.scale(image, (800, 600))

    



if __name__ == '__main__':
    #Creates the game, and runs it
    ai = HackHeartvard()
    ai.run_game()

