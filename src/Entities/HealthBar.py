import pygame

class HealthBar:
    def __init__(self, enemy, height=13):
        self.enemy = enemy
        self.height = height
        self.font = pygame.font.Font(None, 26)  # Fonte para exibir o HP

    def draw(self, surface):
        # Atualiza a largura da barra com base no tamanho do inimigo
        width = self.enemy.rect.width

        # Calcula a proporção da barra de vida
        health_ratio = max(self.enemy.health / self.enemy.max_health, 0)

        # Define as cores
        bar_color = (0, 255, 0)  # Verde
        if health_ratio < 0.5:
            bar_color = (255, 255, 0)  # Amarelo
        if health_ratio < 0.25:
            bar_color = (255, 0, 0)  # Vermelho

        # Posição da barra de vida
        bar_x = self.enemy.rect.left  # Começa no mesmo ponto do inimigo
        bar_y = self.enemy.rect.top - 15

        # Desenha a barra vazia (fundo cinza)
        pygame.draw.rect(surface, (128, 128, 128), (bar_x, bar_y, width, self.height))

        # Desenha a barra preenchida (cor correspondente ao HP)
        pygame.draw.rect(surface, bar_color, (bar_x, bar_y, int(width * health_ratio), self.height))

        # Renderiza o texto com o nome do inimigo e HP
        text_surface = self.font.render(f"{self.enemy.name}: {self.enemy.health}/{self.enemy.max_health}", True,
                                        (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.enemy.rect.centerx, bar_y - 10))
        surface.blit(text_surface, text_rect)
