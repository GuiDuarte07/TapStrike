from pygame import Surface

from src.Entities.Backgound import Background
from src.Entities.Level import Level
from src.Entities.Player import Player
from src.Factories.EnemyFactory import EnemyFactory


class LevelFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_level(window: Surface, level: int, player: Player) -> Level | None:
        if level < 1: return None

        if level <= 10:
            return Level(
                window,
                "Campos montanhosos",
                level,
                player,
                EnemyFactory.rand_enemy_list(10, level*6 + 10, 3, True),
                Background("Campos montanhosos", "mountainous_fields_bg.jpg")
            )

        if level <= 20:
            return Level(
                window,
                "Abismo Desconhecido",
                level,
                player,
                EnemyFactory.rand_enemy_list(10, level * 9 + 30, 20, True),
                Background("Abismo Desconhecido", "unknown_abyss_bg.jpg")
            )

        return None