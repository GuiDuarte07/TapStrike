from src.Entities.Ally import Ally


class Player:
    def __init__(self, gold: int, level: int, skill_level: int, allies=None):
        if allies is None:
            allies = []
        self.gold = gold
        self.level = level
        self.skill_level = skill_level
        self.allies = allies
        self.skill_cd_ms = 3000  # skill cooldown milliseconds

    def click_damage(self):
        return self.level

    def skill_damage(self):
        return self.skill_level * 10

    def gold_to_up(self):
        return self.level * 5

    def level_up(self) -> bool:
        if self.gold < self.gold_to_up():
            return False

        self.gold -= self.gold_to_up()
        self.level += 1
        return True

    def gold_to_up_skill(self):
        return self.skill_level * 30 + 30

    def level_up_skill(self) -> bool:
        if self.gold < self.gold_to_up_skill():
            return False

        self.gold -= self.gold_to_up_skill()
        self.skill_level += 1
        return True

    def upgrade_buy_ally(self, ally_up: Ally) -> bool:
        print(ally_up, 43)
        ally = next((ally for ally in self.allies if ally.name == ally_up.name), None)
        print(ally, 45)
        if ally:
            if self.gold < ally.gold_to_up():
                return False

            self.spend_gold(ally.gold_to_up())
            ally.level_up()

        else:
            if self.gold < ally_up.gold_to_up():
                return False

            self.spend_gold(ally_up.gold_to_up())
            self.allies.append(ally_up)

        return True


    def earn_gold(self, gold: int):
        self.gold += gold

    def spend_gold(self, gold: int):
        self.gold -= gold

