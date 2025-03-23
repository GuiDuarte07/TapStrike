#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Entities import Enemy
from code.Entities.Backgound import Background
from code.Entities.ImposingWarriorAlly import ImposingWarriorAlly
from code.Entities.Player import Player
from code.Entities.RapierWarriorAlly import RapierWarriorAlly


class Level:
    def __init__(self, window: Surface, name: str, level: int, enemies:list[Enemy], bg:Background):
        self.window = window
        self.name = name
        self.level = level
        self.enemies = enemies
        self.bg = bg

    def run(self) -> bool:
        #pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        #pygame.mixer_music.set_volume(0.3)
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()


        player = Player(0, 1, 0)


        while True:
            self.window.blit(source=self.bg.surf, dest=self.bg.rect)
            clock.tick(60)
            if len(self.enemies) > 0:
                self.window.blit(source=self.enemies[0].surf, dest=self.enemies[0].rect)
            else:
                print(f"Level {self.level} - Concluído!")
                return True
            for ally in player.allies:
                self.window.blit(source=ally.surf, dest=ally.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
