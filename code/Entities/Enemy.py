from typing import Literal

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entities.Entity import Entity

EnemyType = Literal['normal', 'boss']

class Enemy(Entity):
    def __init__(self, name: str, asset: str, health: int, drop_gold: int, enemy_type:EnemyType = 'normal'):
        super().__init__(name, asset, (WIN_WIDTH/2, WIN_HEIGHT/2))
        self.enemy_type = enemy_type
        self.health = health if enemy_type == 'normal' else health * 2
        self.drop_gold = drop_gold
