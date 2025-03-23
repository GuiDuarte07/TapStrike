from code.Entities.Ally import Ally


class Player:
    def __init__(self, gold: int, base_attack_level: int, skill_level: int, allies=None):
        if allies is None:
            allies = []
        self.gold = gold
        self.base_attack_level = base_attack_level
        self.skill_level = skill_level
        self.allies = allies
        self.skill_cd_ms = 3000  # skill cooldown milliseconds

    def base_attack_damage(self):
        return self.base_attack_level

    def skill_damage(self):
        return self.skill_level * 10

    def gold_to_up_base_attack(self):
        return self.base_attack_level * 5

    def gold_to_up_skill(self):
        return self.skill_level * 30 + 30

    def level_up_base_attack(self):
        self.base_attack_level += 1

    def level_up_skill(self):
        self.skill_level += 1

