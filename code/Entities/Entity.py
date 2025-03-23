from abc import ABC
import pygame.image



class Entity(ABC):
    def __init__(self, name: str, asset: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + asset).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
