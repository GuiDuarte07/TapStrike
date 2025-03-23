import pygame
from pygame import Rect
from src.Entities.Player import Player
from src.Entities.Enemy import Enemy


class DpsHandler:
    def __init__(self, player: Player, enemies: list[Enemy]):
        self.player = player
        self.enemies = enemies
        self.DPS_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.DPS_EVENT, 1000)

    def handle_dps(self, event: pygame.event.Event):
        """Verifica se o evento DPS_EVENT foi ativo e aplica o dps dos aliados"""
        if event.type == self.DPS_EVENT:
            print("Clock!")

            enemy = self.enemies[0]

            total_dps = sum(ally.dps for ally in self.player.allies)
            enemy.take_damage(total_dps)
            if enemy.is_dead():
                self.enemies.remove(enemy)  # Remove inimigo se estiver morto
                self.player.earn_gold(enemy.drop_gold)
