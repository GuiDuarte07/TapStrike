import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Factories.LevelFactory import LevelFactory


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("TapStrike")

    def run(self):
        while True:
            level = LevelFactory.get_level(self.window, 1)
            level.run()

            # menu = Menu(self.window)
            # menu_return = menu.run()

            pygame.quit()
            sys.exit()
