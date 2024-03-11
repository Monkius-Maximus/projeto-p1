import pygame as pg

class Mapa():
    def __init__(self, imagem_mapa):
        self.image = imagem_mapa
    
    def draw(self, surface):
        surface.blit(self.image, (0, 0))