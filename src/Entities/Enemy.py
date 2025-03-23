from typing import Literal

import pygame

from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.Entities.Entity import Entity
from src.Entities.HealthBar import HealthBar

EnemyType = Literal['normal', 'boss']

class Enemy(Entity):
    def __init__(self, name: str, asset: str, health: int, drop_gold: int, enemy_type:EnemyType = 'normal'):
        super().__init__(name, asset, (0,0))
        self.enemy_type = enemy_type
        self.max_health = health if enemy_type == 'normal' else health * 2
        self.health = self.max_health
        self.drop_gold = drop_gold
        self.rect.centerx = WIN_WIDTH/2
        self.rect.centery = WIN_HEIGHT/2 + 100
        self.health_bar = HealthBar(self)

    def take_damage(self, damage: int):
        """Reduz a vida do inimigo quando atingido."""
        self.health -= damage

    def is_dead(self) -> bool:
        """Retorna True se o inimigo estiver sem vida."""
        return self.health <= 0

    def draw(self, surface):
        """Desenha o inimigo e a barra de vida."""
        surface.blit(self.surf, self.rect)
        self.health_bar.draw(surface)