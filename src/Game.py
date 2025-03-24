import sys

import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.Entities.Player import Player
from src.Factories.LevelFactory import LevelFactory
from src.manages.SaveManager import SaveManager


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.save_manager = SaveManager()
        data = self.save_manager.load()
        self.player = data["player"]
        self.last_level = data["last_level"]


    def run(self):
        pygame.display.set_caption("TapStrike")

        while True:
            for i in range(self.last_level, 21):
                pygame.mouse.set_cursor(pygame.cursors.arrow)
                level = LevelFactory.get_level(self.window, i, self.player)
                level.run()

                self.save_manager.save(self.player, i)

            pygame.quit()
            sys.exit()
