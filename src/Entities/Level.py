import sys

import pygame
from pygame import Surface, Rect
from pygame.examples.moveit import WIDTH, HEIGHT
from pygame.font import Font

from src.Entities import Enemy
from src.Entities.Backgound import Background
from src.Entities.Player import Player
from src.event.ClickHandler import ClickHandler
from src.event.DpsHandler import DpsHandler
from src.view.UpgradeMenu import UpgradeMenu


class Level:
    def __init__(self, window: Surface, name: str, level: int, player: Player, enemies:list[Enemy], bg:Background, bg_sound_path:str):
        self.window = window
        self.name = name
        self.level = level
        self.player = player
        self.enemies = enemies
        self.bg = bg
        self.bg_sound_path = bg_sound_path
        self.click_handler = None
        self.dps_handler = None
        self.font = pygame.font.SysFont("Arial", 26)


    def run(self) -> bool:
        pygame.mixer_music.load(self.bg_sound_path)
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        self.click_handler = ClickHandler(self.player, self.enemies)
        self.dps_handler = DpsHandler(self.player, self.enemies)

        from src.view.HUD import HUD
        hud = HUD(self.window, self.player, self)
        upgrade_menu = UpgradeMenu(self.window, self.player)


        while True:
            clock.tick(60)
            self.window.blit(source=self.bg.surf, dest=self.bg.rect)


            if len(self.enemies) > 0:
                self.enemies[0].draw(self.window)
                #self.window.blit(source=self.enemies[0].surf, dest=self.enemies[0].rect)
            else:
                print(f"Level {self.level} - Concluído!")
                return True
            for ally in self.player.allies:
                self.window.blit(source=ally.surf, dest=ally.rect)

            upgrade_menu.draw()
            hud.draw()

            skill_box_rect = self._draw_skill_btn()

            #  -- Event Loop --
            for event in pygame.event.get():
                upgrade_menu.handle_event(event) #Eventos do menu de upgrade
                if upgrade_menu.is_expanded is False:
                    self.click_handler.handle_click(event)  # Enviar evento para o handle_click
                    self.click_handler.handle_skill_click(event, skill_box_rect)

                self.dps_handler.handle_dps(event)
                self.dps_handler.handle_skill_cd(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def _draw_skill_btn(self) -> Rect|None:
        if self.player.enable_skill is False or self.player.skill_level == 0: return None
        box_rect = pygame.Rect((WIDTH // 2 - 130, 70, 100, 45))
        # Desenha a caixa arredondada
        pygame.draw.rect(self.window, (128,128,128), box_rect, border_radius=15)

        # Renderiza o texto
        text_surface = self.font.render("Skill", True, (255,255,255))
        text_rect = text_surface.get_rect(center=box_rect.center)

        self.window.blit(text_surface, text_rect)


        return box_rect