import pygame as pg
import math

class Torre(pg.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.range = 120
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.alvo = None

    def update(self, grupo_inimigos):
        self.selecionar_alvo(grupo_inimigos)

    def selecionar_alvo(self, grupo_inimigos):
        x_dist = 0
        y_dist = 0
        for inimigo in grupo_inimigos:
            #calcula a distância entre a torre e cada inimigo com base na posição x e y do retângulo da torre
            x_dist = inimigo.pos[0] - self.rect.x
            y_dist = inimigo.pos[1] - self.rect.y
            #Distancia entre a torre e o inimigo ())
            dist = math.sqrt(x_dist**2 + y_dist**2)
            if dist < self.range:
                self.alvo = inimigo
                print('alvo selecionado')