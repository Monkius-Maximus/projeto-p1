import pygame
from constants import *
from mapa import *
from hud import *
from inimigos import *
from botoes import *
pygame.init()

#clock
clock = pygame.time.Clock()

#setup da janela do jogo
win = pygame.display.set_mode((SCREEN_HEIGHT + SIDE_BAR, SCREEN_WIDTH))
pygame.display.set_caption("Projeto P1")
#carregando imagens
imagem_mapa = pygame.image.load('imagens/mapa.png').convert_alpha()
image_side = pygame.image.load('imagens/madeira.jpg').convert_alpha()
imagem_inimigo = pg.image.load('imagens/inimigo.png').convert_alpha()
imagem_compra_torre = pg.image.load('imagens/botão_torre.png').convert_alpha()
#mundo
mundo = Mapa(imagem_mapa)
sidebar = Lateral(image_side)
#criação de grupos
grupo_inimigos = pg.sprite.Group()
inimigo = Inimigo(caminho, imagem_inimigo)
grupo_inimigos.add(inimigo)

#criação dos botoes
compra_torre = Botão(SCREEN_HEIGHT + 30, 100, imagem_compra_torre)


#loop
run = True
while run:
    
    clock.tick(FPS)
    
    #updates
    grupo_inimigos.update()
    
    
    #desenhos
    grupo_inimigos.draw(win)
    
    
    mundo.draw(win)
    
    sidebar.draw(win)
    if compra_torre.draw(win):
        print('torre comprada')
    #loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
