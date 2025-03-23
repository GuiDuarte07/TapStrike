from abc import ABC, abstractmethod
from code.Entities.Entity import Entity


class Ally(Entity, ABC):
    def __init__(self, name: str, asset: str, position: tuple, initial_gold_cust: int, level: int):
        super().__init__(name, asset, position)
        self.level = level
        self.dps = 0
        self._calc_dps()
        self.initial_gold_cust = initial_gold_cust

    def level_up(self):
        self.level += 1
        self._calc_dps()

    @abstractmethod
    def _calc_dps(self):
        pass

    @abstractmethod
    def gold_to_up(self):
        pass



