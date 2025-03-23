#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Entities import Enemy
from code.Entities.Backgound import Background


class Level:
    def __init__(self, window: Surface, name: str, level: int, enemies:list[Enemy], bg:Background):
        self.window = window
        self.name = name
        self.enemies = enemies
        self.bg = bg

    def run(self):
        #pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        #pygame.mixer_music.set_volume(0.3)
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            self.window.blit(source=self.bg.surf, dest=self.bg.rect)
            clock.tick(60)
            for enemy in self.enemies:
                self.window.blit(source=enemy.surf, dest=enemy.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
