from src.Entities.Ally import Ally


class ImposingWarriorAlly(Ally):
    def __init__(self, level: int = 1):
        super().__init__("ImposingWarrior", "Guerreiro Imponente", "imposing_warrior_ally.png", (32,32), 35, level)

    def gold_to_up(self):
        return self.level * self.initial_gold_cust

    def _calc_dps(self):
        self.dps = self.level * 3 + 3