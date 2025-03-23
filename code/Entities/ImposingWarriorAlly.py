from code.Entities.Ally import Ally


class ImposingWarriorAlly(Ally):
    def __init__(self, level: int = 1):
        super().__init__("Guerreiro Imponente", "imposing_warrior_ally.png", (32,32), 35, level)

    def __gold_to_up(self):
        self.gold_to_up = self.level * self.initial_gold_cust

    def __calc_dps(self):
        self.dps = self.level * 3 + 3