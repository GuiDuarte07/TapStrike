from src.Entities.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, asset: str):
        super().__init__(name, asset, (0, 0))