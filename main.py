import pygame
from constants import *
from mapa import *
from hud import *
pygame.init()

#clock
clock = pygame.time.Clock()

#setup da janela do jogo
win = pygame.display.set_mode((SCREEN_HEIGHT + SIDE_BAR, SCREEN_WIDTH))
pygame.display.set_caption("Projeto P1")
imagem_mapa = pygame.image.load('imagens/mapa.png').convert_alpha()
image_side = pygame.image.load('imagens/madeira.jpg').convert_alpha()
#mundo
mundo = Mapa(imagem_mapa)
sidebar = Lateral(image_side)



#loop
run = True
while run:
    clock.tick(FPS)
    win.fill('blue')
    mundo.draw(win)
    sidebar.draw(win)
    #loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
