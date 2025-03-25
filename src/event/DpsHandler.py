import pygame
from pygame import Rect
from src.Entities.Player import Player
from src.Entities.Enemy import Enemy


class DpsHandler:
    def __init__(self, player: Player, enemies: list[Enemy]):
        self.player = player
        self.enemies = enemies
        self.DPS_EVENT = pygame.USEREVENT + 1
        self.SKILL_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.DPS_EVENT, 1000)
        pygame.time.set_timer(self.SKILL_EVENT, self.player.skill_cd_ms)

    def handle_skill_cd(self, event: pygame.event.Event):
        """Verifica se o evento SKILL_EVENT foi ativado para liberar o uso da skill"""
        if event.type == self.SKILL_EVENT:
            self.player.enable_skill = True


    def handle_dps(self, event: pygame.event.Event):
        """Verifica se o evento DPS_EVENT foi ativo e aplica o dps dos aliados"""

        if len(self.enemies) == 0: return

        if event.type == self.DPS_EVENT:
            enemy = self.enemies[0]

            total_dps = sum(ally.dps for ally in self.player.allies)
            enemy.take_damage(total_dps)
            if enemy.is_dead():
                self.enemies.remove(enemy)  # Remove inimigo se estiver morto
                self.player.earn_gold(enemy.drop_gold)
