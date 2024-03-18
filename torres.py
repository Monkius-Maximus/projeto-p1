import pygame as pg
import math
from constants import *
from constants import *

class Torre(pg.sprite.Sprite):
    def __init__(self, sprite_sheet, position, mundo):
        super().__init__()
        self.range = 120
        self.alvo = None
        self.ultimo_tiro = pg.time.get_ticks()
        self.cooldown = 600
        self.selecionado = False
        
        #variaveis de animação
        self.sprite_sheet = sprite_sheet
        self.lista_animacao = self.carregar_animacao()
        self.index_animacao = 0
        self.tempo_att = pg.time.get_ticks()
        
        #atualizando animação
        self.image = self.lista_animacao[self.index_animacao]
        self.rect = self.image.get_rect(center=position)

        
    def carregar_animacao(self):
        #extrair imagens do sprite sheet
        tamanho = self.sprite_sheet.get_height()
        lista_animacao = []
        for i in range(etapas_animacao):
            temp_img = self.sprite_sheet.subsurface(i * tamanho, 0, tamanho, tamanho)
            lista_animacao.append(temp_img)
        return lista_animacao
        
    def update(self, grupo_inimigos, mundo):
        if self.alvo:
            self.animacao(mundo)
        else:
            if pg.time.get_ticks() - self.ultimo_tiro > (self.cooldown / mundo.velocidade_nivel):
                self.selecionar_alvo(grupo_inimigos)
    
    
    def animacao(self, mundo):
        #atualizar imagem
        self.image = self.lista_animacao[self.index_animacao]
        #checando se tempo o suficiente ja passou
        if pg.time.get_ticks() - self.tempo_att > (delay_animacao / mundo.velocidade_nivel):
            self.tempo_att = pg.time.get_ticks()
            self.index_animacao += 1
        #checando se a animação acabou e resetando pra primeira posicao
            if self.index_animacao >= etapas_animacao:
                self.index_animacao = 0
                self.ultimo_tiro = pg.time.get_ticks()
                self.alvo = None
                
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selecionado:
            surface.blit(self.imagem_range, self.range_rect)
        
    
    def selecionar_alvo(self, grupo_inimigos):
        x_dist = 0
        y_dist = 0
        for inimigo in grupo_inimigos:
            if inimigo.vida > 0:   
                #calcula a distância entre a torre e cada inimigo com base na posição x e y do retângulo da torre
                x_dist = inimigo.pos[0] - self.rect.x
                y_dist = inimigo.pos[1] - self.rect.y
                #Distancia entre a torre e o inimigo ())
                dist = math.sqrt(x_dist**2 + y_dist**2)
                if dist < self.range:
                    self.alvo = inimigo
                    print('alvo selecionado')
                    self.alvo.vida -= DANO
                    break
            #calcula a distância entre a torre e cada inimigo com base na posição x e y do retângulo da torre
            x_dist = inimigo.pos[0] - self.rect.x
            y_dist = inimigo.pos[1] - self.rect.y
            #Distancia entre a torre e o inimigo
            dist = math.sqrt(x_dist**2 + y_dist**2)
            if dist < self.range:
                self.alvo = inimigo
                self.alvo.vida -= DANO
                print('alvo selecionado')
                break