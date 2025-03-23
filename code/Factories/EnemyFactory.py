import random
from typing import Literal, get_args

from code.Entities.Enemy import Enemy, EnemyType

EnemySprite = Literal[
    'AlienSoldier',
    'BossOgre',
    'BrainlessDemon',
    'CaptainOgre',
    'ClubOgre',
    'ContaminatedBat',
    'CunningOgre',
    'EvilDemon',
    ]

enemy_sprites = get_args(EnemySprite)

class EnemyFactory:

    @staticmethod
    def get_enemy(identify: EnemySprite, health: int, drop_gold: int, enemy_type: EnemyType) -> Enemy | None:
        match identify:
            case 'AlienSoldier':
                return Enemy('Alien Soldado', 'alien_soldier_enemy.png', health, drop_gold, enemy_type)
            case 'BossOgre':
                return Enemy('Ogro Chefão', 'boss_ogre_enemy.png', health, drop_gold, enemy_type)
            case 'CaptainOgre':
                return Enemy('Capitão Ogro', 'captain_ogre_enemy.png', health, drop_gold, enemy_type)
            case 'ClubOgre':
                return Enemy('Ogro de Porrete', 'club_ogre_enemy.png', health, drop_gold, enemy_type)
            case 'ContaminatedBat':
                return Enemy('Morcego Contaminado', 'contaminated_bat_enemy.png', health, drop_gold, enemy_type)
            case 'CunningOgre':
                return Enemy('Ogro Astuto', 'cunning_ogre_enemy.png', health, drop_gold, enemy_type)
            case 'BrainlessDemon':
                return Enemy('Ogro Sem Cerébro', 'brainless_demon_enemy.png', health, drop_gold, enemy_type)
            case 'EvilDemon':
                return Enemy('Demônio Maligno', 'evil_demon_enemy.png', health, drop_gold, enemy_type)

        return None

    @staticmethod
    def rand_enemy_list(list_size: int, initial_health: int, initial_drop_gold: int, has_boss: bool):
        enemies = []
        for i in range(list_size):
            enemies.append(
                EnemyFactory.get_enemy(
                    random.choice(enemy_sprites),
                    initial_health,
                    initial_drop_gold,
                    'normal' if has_boss is False or (has_boss and i != list_size - 1) else 'boss'
                )
            )

        return enemies
