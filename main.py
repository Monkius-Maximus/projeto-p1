import pygame as pg
from constants import *
from mapa import *
from hud import *
from inimigos import *
from botoes import *
from torres import *

pg.init()

# clock
clock = pg.time.Clock()

# setup da janela do jogo
win = pg.display.set_mode((SCREEN_HEIGHT + SIDE_BAR, SCREEN_WIDTH))
pg.display.set_caption("Projeto P1")

# carregando imagens
imagem_mapa = pg.image.load('imagens/mapa.png').convert_alpha()
image_side = pg.image.load('imagens/madeira.jpg').convert_alpha()
imagem_inimigo = pg.image.load('imagens/inimigo.png').convert_alpha()
imagem_compra_torre = pg.image.load('imagens/botão_torre.png').convert_alpha()
imagem_torre = pg.image.load('imagens/torretas1_1.png').convert_alpha()

# mundo
mundo = Mapa(imagem_mapa)
sidebar = Lateral(image_side)

# criação de grupos
grupo_inimigos = pg.sprite.Group()
inimigo = Inimigo(caminho, imagem_inimigo)
grupo_inimigos.add(inimigo)
grupo_torres = pg.sprite.Group()  # Grupo para torres

# criação dos botões
compra_torre = Botão(SCREEN_HEIGHT + 30, 100, imagem_compra_torre)

# Loop principal do jogo
run = True
aguardando_posicao_torre = False  # Variável de controle para a colocação da torre
while run:
    
    clock.tick(FPS)
    
    # Verifica eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN: 
            if compra_torre.rect.collidepoint(event.pos):  
                print('Clique no botão de compra de torre')
                # Define uma variável de controle para a criação da torre no próximo clique do botão direito
                aguardando_posicao_torre = True
            elif event.button == 3 and aguardando_posicao_torre: 
                print('Clique com o botão direito')
                nova_torre = Torre(imagem_torre, event.pos) 
                grupo_torres.add(nova_torre) 
                aguardando_posicao_torre = False 

    # Atualizações
    grupo_inimigos.update()
    grupo_torres.update()

    # Desenhos
    win.fill((0, 0, 0))  # Preenche a tela com a cor preta
    mundo.draw(win)
    sidebar.draw(win)
    grupo_inimigos.draw(win)
    grupo_torres.draw(win)
    compra_torre.draw(win)

    pg.display.update()

pg.quit()
