import pygame

from src.Const import WIN_HEIGHT
from src.Entities.ImposingWarriorAlly import ImposingWarriorAlly
from src.Entities.Player import Player
from src.Entities.RapierWarriorAlly import RapierWarriorAlly


class UpgradeMenu:
    def __init__(self, window: pygame.Surface, player: Player):
        self.window = window
        self.player = player
        self.width = window.get_width()
        self.height = 60  # Altura da barra quando contraída
        self.expanded_height = 220  # Altura quando expandido
        self.is_expanded = False
        self.bg_color = (50, 50, 50)  # Cor de fundo do menu
        self.button_color = (70, 70, 70)
        self.hover_color = (100, 100, 100)
        self.font = pygame.font.SysFont('Lucida Sans Typewriter', 10)
        self.buttons = self.button_set()


    def button_set(self):
        imposing_warrior = next((ally for ally in self.player.allies if isinstance(ally, ImposingWarriorAlly)), None)
        text_to_imposing_warrior = "Melhorar" if imposing_warrior else "Comprar"
        text_to_imposing_warrior += " Guerreiro Destemido - "
        text_to_imposing_warrior += f"{imposing_warrior.gold_to_up() if imposing_warrior else ImposingWarriorAlly().initial_gold_cust}G"

        rapier_warrior = next((ally for ally in self.player.allies if isinstance(ally, RapierWarriorAlly)), None)
        text_to_rapier_warrior = "Melhorar" if rapier_warrior else "Comprar"
        text_to_rapier_warrior += " Guerreiro de Florete - "
        text_to_rapier_warrior += f"{rapier_warrior.gold_to_up() if rapier_warrior else RapierWarriorAlly().initial_gold_cust}G"

        def upgrade_imposing():
            """Ação para melhorar/comprar o Guerreiro Destemido"""
            if imposing_warrior:
                return self.player.upgrade_buy_ally(imposing_warrior)
            else:
                return self.player.upgrade_buy_ally(ImposingWarriorAlly())

        def upgrade_rapier():
            """Ação para melhorar/comprar o Guerreiro de Florete"""
            if rapier_warrior:
                return self.player.upgrade_buy_ally(rapier_warrior)
            else:
                return self.player.upgrade_buy_ally(RapierWarriorAlly())

        # Botões (posição relativa)
        return {
            "up_click": {
                'text': f"Melhorar clique - {self.player.gold_to_up()}G",
                'rect': pygame.Rect(10, WIN_HEIGHT - self.expanded_height + 20, 150, 40),
                'on_click': self.player.level_up
            },
            "up_skill": {
                'text': f"Upgrade Skill - {self.player.gold_to_up_skill()}G",
                'rect': pygame.Rect(10, WIN_HEIGHT - self.expanded_height + 100, 150, 40),
                'on_click': self.player.level_up_skill
            },
            "up_imposing": {
                'text': text_to_imposing_warrior,
                'rect': pygame.Rect(self.width - 280, WIN_HEIGHT - self.expanded_height + 20, 260, 40),
                'on_click': upgrade_imposing
            },
            "up_rapier": {
                'text': text_to_rapier_warrior,
                'rect': pygame.Rect(self.width - 280, WIN_HEIGHT - self.expanded_height + 100, 260, 40),
                'on_click': upgrade_rapier
            }
        }


    def draw(self):
        """Desenha o menu na tela"""
        menu_height = self.expanded_height if self.is_expanded else self.height
        pygame.draw.rect(self.window, self.bg_color, (0, self.window.get_height() - menu_height, self.width, menu_height))

        cursor_changed = False  # Flag para mudar o cursor

        # Desenha os botões se o menu estiver expandido
        if self.is_expanded:
            mouse_pos = pygame.mouse.get_pos()
            for _, btn in self.buttons.items():
                if btn["rect"].collidepoint(mouse_pos):
                    cursor_changed = True
                    color = self.hover_color
                else:
                    color = self.button_color

                pygame.draw.rect(self.window, color, btn["rect"])
                self.draw_text(btn["text"], btn["rect"].center)

        if not cursor_changed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw_text(self, text, position):
        """Renderiza o texto no centro do botão"""
        text_surf = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=position)
        self.window.blit(text_surf, text_rect)

    def toggle_menu(self):
        """Alterna entre expandido e contraído"""
        self.is_expanded = not self.is_expanded

    def handle_event(self, event):
        """Lida com os eventos de clique"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            menu_top = self.window.get_height() - self.height
            if not self.is_expanded and y >= menu_top:  # Clica na barra para expandir
                self.toggle_menu()
            elif self.is_expanded:
                for _, btn in self.buttons.items():
                    if btn["rect"].collidepoint(event.pos):
                        result = btn["on_click"]()
                        print(f"{btn["text"]} foi clicado!" , " Erro: Dinheiro insuficiente" if result is False else "Item comprado!")
                        if result:
                            self.buttons = self.button_set()

            self.close_if_clicked_outside(event)

    def close_if_clicked_outside(self, event):
        """Fecha o menu se o clique for fora da área expandida"""
        if self.is_expanded:
            menu_top = self.window.get_height() - self.expanded_height  # Topo do menu expandido
            if event.pos[1] < menu_top:  # Se o clique for acima do menu
                self.toggle_menu()
