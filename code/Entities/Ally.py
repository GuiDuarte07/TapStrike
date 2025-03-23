from abc import ABC, abstractmethod
from code.Entities.Entity import Entity


class Ally(Entity, ABC):
    def __init__(self, name: str, asset: str, position: tuple, initial_gold_cust: int, level: int):
        super().__init__(name, position)
        self.level = level
        self.dps = 0
        self.__calc_dps()
        self.initial_gold_cust = initial_gold_cust
        self.gold_to_up = 0
        self.__gold_to_up()

    def level_up(self):
        self.level += 1
        self.__gold_to_up()
        self.__calc_dps()

    @abstractmethod
    def __calc_dps(self):
        pass
    @abstractmethod
    def __gold_to_up(self):
        pass



