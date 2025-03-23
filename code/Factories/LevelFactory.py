from pygame import Surface

from code.Entities.Backgound import Background
from code.Entities.Level import Level


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
                [],
                Background("Campos montanhosos", "mountainous_fields_bg.jpg")
            )

        return None