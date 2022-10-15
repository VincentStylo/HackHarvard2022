import pygame
from time import sleep


def Move(x):
    while True:
        for event in pygame.event.get():
            while event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    x += 10
                if event.key == pygame.K_a:
                    x -= 10
                return x


def Jump(y):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y -= 20
                return y
