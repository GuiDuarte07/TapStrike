import pygame
from pygame import Rect
from src.Entities.Player import Player
from src.Entities.Enemy import Enemy

class ClickHandler:
    def __init__(self, player: Player, enemies: list[Enemy]):
        self.player = player
        self.enemies = enemies

    def handle_click(self, event: pygame.event.Event):
        """Verifica se o clique atingiu algum inimigo e aplica o dano."""

        if len(self.enemies) == 0: return

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            enemy = self.enemies[0]
            if enemy.rect.collidepoint(mouse_pos):  # Verifica se o clique foi no inimigo
                enemy.take_damage(self.player.click_damage())
                if enemy.is_dead():
                    self.enemies.remove(enemy)  # Remove inimigo se estiver morto
                    self.player.earn_gold(enemy.drop_gold)


        # código de debbug que não deve ir para produção, apenas para facilitar testes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # Verifica se a tecla espaço está pressionada
            print("Segurando a tecla espaço!")
            enemy = self.enemies[0]
            enemy.take_damage(self.player.click_damage())
            if enemy.is_dead():
                self.enemies.remove(enemy)  # Remove inimigo se estiver morto
                self.player.earn_gold(enemy.drop_gold)

    def handle_skill_click(self, event: pygame.event.Event, skill_box_rect: Rect|None):
        if len(self.enemies) == 0 or skill_box_rect is None: return

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            enemy = self.enemies[0]
            if skill_box_rect.collidepoint(mouse_pos):  # Verifica clique no botão de habilidade
                enemy.take_damage(self.player.skill_damage())
                if enemy.is_dead():
                    self.enemies.remove(enemy)  # Remove inimigo se estiver morto
                    self.player.earn_gold(enemy.drop_gold)
