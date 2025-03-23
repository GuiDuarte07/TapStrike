#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import WIN_WIDTH
from src.Entities import Enemy
from src.Entities.Backgound import Background
from src.Entities.ImposingWarriorAlly import ImposingWarriorAlly
from src.Entities.Player import Player
from src.Entities.RapierWarriorAlly import RapierWarriorAlly
from src.event.ClickHandler import ClickHandler
from src.event.DpsHandler import DpsHandler
from src.view.UpgradeMenu import UpgradeMenu


class Level:
    def __init__(self, window: Surface, name: str, level: int, enemies:list[Enemy], bg:Background):
        self.window = window
        self.name = name
        self.level = level
        self.enemies = enemies
        self.bg = bg
        self.click_handler = None
        self.dps_handler = None

    def run(self) -> bool:
        #pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        #pygame.mixer_music.set_volume(0.3)
        #pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()


        player = Player(1202, 1, 0)
        self.click_handler = ClickHandler(player, self.enemies)
        self.dps_handler = DpsHandler(player, self.enemies)

        upgrade_menu = UpgradeMenu(self.window, player)


        while True:
            clock.tick(60)
            self.window.blit(source=self.bg.surf, dest=self.bg.rect)
            self.text_screen(23, f"Gold: {player.gold}",(0,0,0), (30, 10))


            if len(self.enemies) > 0:
                self.enemies[0].draw(self.window)
                #self.window.blit(source=self.enemies[0].surf, dest=self.enemies[0].rect)
            else:
                print(f"Level {self.level} - Concluído!")
                return True
            for ally in player.allies:
                self.window.blit(source=ally.surf, dest=ally.rect)

            upgrade_menu.draw()

            #  -- Event Loop --
            for event in pygame.event.get():
                upgrade_menu.handle_event(event) #Eventos do menu de upgrade
                if upgrade_menu.is_expanded is False:
                    self.click_handler.handle_click(event)  # Enviar evento para o handle_click

                self.dps_handler.handle_dps(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def text_screen(self, font_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(None, size=font_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)