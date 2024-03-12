import pygame as pg 

class Botão():
    def __init__(self, x, y, imagem):
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        acao = False
        #conseguir posição do mouse
        pos = pg.mouse.get_pos()
        
        #checar se mouse esta sobre o botão e se ele foi apertado
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                acao = True
                self.clicked = True
        #o [0] significa o botão esquerdo do mouse, e o == 0 significa que ele não esta sendo apertado, == 1 significa q ele foi apertado
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #desenhar botão na tela
        surface.blit(self.image, self.rect)
        
        return acao