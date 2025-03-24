import pygame
from pygame import Surface

from src.Entities.Level import Level
from src.Entities.Player import Player


class HUD:
    def __init__(self, window: Surface, player: Player, level: Level):
        self.window = window
        self.player = player
        self.level = level
        self.width = window.get_width()
        self.height = 50  # Altura da HUD
        self.text_color = (205,121,71)  # Cor do texto
        self.font = pygame.font.SysFont('Lucida Sans Typewriter', 16)

    def draw(self):
        # Textos
        gold_text = f"Gold: {self.player.gold}"
        level_text = f"{self.level.name} - Level {self.level.level}"
        counter_text = f"{11 - len(self.level.enemies)}/10"

        # Renderiza os textos
        gold_surface = self.font.render(gold_text, True, self.text_color)
        level_surface = self.font.render(level_text, True, self.text_color)
        counter_surface = self.font.render(counter_text, True, self.text_color)

        # Obtém os retângulos para posicionamento
        gold_rect = gold_surface.get_rect(topleft=(10, 8))  # Esquerda
        level_rect = level_surface.get_rect(center=(self.width // 2, 40))  # Centro
        counter_rect = counter_surface.get_rect(topright=(self.width - 10, 8))  # Direita

        # Desenha os textos na tela
        self.window.blit(gold_surface, gold_rect)
        self.window.blit(level_surface, level_rect)
        self.window.blit(counter_surface, counter_rect)

