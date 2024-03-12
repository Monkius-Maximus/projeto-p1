import pygame as pg
from pygame.math import Vector2



class Inimigo(pg.sprite.Sprite):
    def __init__(self, caminhos, imagem):
        pg.sprite.Sprite.__init__(self)
        self.caminhos = caminhos
        self.pos = Vector2(self.caminhos[0])
        self.target_caminho = 1
        self.velocidade = 4
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self):
        self.andar()    
    
    def andar(self):
        if self.target_caminho < len(self.caminhos):
            self.target = Vector2(self.caminhos[self.target_caminho])
            self.movimento = self.target - self.pos
        else:
            #inimigo chegou ao fim do caminho
            self.kill()
        
        #calculando distancia até o alvo
        dist = self.movimento.length()
        #checando se a distancia é menor que a velocidade de movimento
        if dist >= self.velocidade:
            self.pos += self.movimento.normalize() * self.velocidade
        else:
            if dist!= 0:
                self.pos += self.movimento.normalize() * dist
            self.target_caminho += 1
        self.rect.center = self.pos