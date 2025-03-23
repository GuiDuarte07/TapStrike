from src.Entities.Ally import Ally
from src.Entities.Player import Player


class RapierWarriorAlly(Ally):
    def __init__(self, level: int = 1):
        super().__init__("Guerreiro de Florete", "rapier_warrior_ally.png", (120,32), 100, level)

    def gold_to_up(self):
        return self.level * self.initial_gold_cust + self.initial_gold_cust

    def _calc_dps(self):
        self.dps = self.level * 5 + 6