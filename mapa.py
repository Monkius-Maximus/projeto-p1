import pygame as pg
from dados_inimigos import dados_spawn
from inimigos import *
from constants import VIDA, DINHEIRO
from random import shuffle
class Mapa():
    def __init__(self, imagem_mapa):
        self.nivel = 1
        self.vida = VIDA
        self.dinheiro = DINHEIRO
        self.image = imagem_mapa
        self.lista_inimigos = []
        self.inimigos_spawnados = 0
        self.inimigos_mortos = 0
        self.inimigos_passaram = 0
        
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
    
    def checa_nivel_completo(self):
        if (self.inimigos_mortos + self.inimigos_passaram) == len(self.lista_inimigos):
            return True
    
    def reseta_nivel(self):
        #reseta variaveis de inimigos
        self.lista_inimigos = []
        self.inimigos_mortos = 0
        self.inimigos_passaram = 0
        self.inimigos_spawnados = 0
            
    def processamento_inimigos(self):
        inimigos = dados_spawn[self.nivel -1]
        for tipos_inimigos in inimigos:
            inimigos_pra_spawnar = inimigos[tipos_inimigos]
            for inimigo in range(inimigos_pra_spawnar):
                self.lista_inimigos.append(tipos_inimigos)
        #randomizador de inimigos
        shuffle(self.lista_inimigos)