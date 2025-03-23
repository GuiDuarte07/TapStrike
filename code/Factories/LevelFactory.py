from pygame import Surface

from code.Entities.Backgound import Background
from code.Entities.Level import Level
from code.Factories.EnemyFactory import EnemyFactory


class LevelFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_level(window: Surface, level: int):
        if level < 1: return None

        if level <= 10:
            return Level(
                window,
                "Campos montanhosos",
                level,
                EnemyFactory.rand_enemy_list(10, 10, 3, True),
                Background("Campos montanhosos", "mountainous_fields_bg.jpg")
            )

        return None