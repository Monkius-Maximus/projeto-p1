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

#fontes para texto
fonte_texto = pg.font.SysFont('Goudy Stout', 24, True)
fonte_texto_grande = pg.font.SysFont('Goudy Stout', 26)

#desenhando textos na tela
def escrita_texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    win.blit(imagem, (x, y))
# carregando imagens

imagem_mapa = pg.image.load('imagens/niveis/mapa.png').convert_alpha()
image_side = pg.image.load('imagens/hud/madeira.jpg').convert_alpha()
imagem_inimigo = {
    'fraco': pg.image.load('imagens/inimigos/inimigo_1.png').convert_alpha(),
    'normal': pg.image.load('imagens/inimigos/inimigo_2.png').convert_alpha(),
    'forte': pg.image.load('imagens/inimigos/inimigo_3.png').convert_alpha()
    }
imagem_compra_torre = pg.image.load('imagens/hud/botao_torre.png').convert_alpha()
imagem_cancelar_compra = pg.image.load('imagens/hud/botao_cancelar_compra.png').convert_alpha()
imagem_iniciar = pg.image.load('imagens/hud/botao_iniciar.png').convert_alpha()
imagem_avancar = pg.image.load('imagens/hud/botao_avancar.png').convert_alpha()
imagem_recomecar = pg.image.load('imagens/hud/botao_recomecar.png').convert_alpha()
imagem_torre = pg.image.load('imagens/torre_1/torretas1_1.png').convert_alpha()
torre_cursor = pg.image.load('imagens/torre_1/torretas1_1.png').convert_alpha()

# mundo
mundo = Mapa(imagem_mapa)
sidebar = Lateral(image_side)
mundo.processamento_inimigos()

# criação de grupos
grupo_inimigos = pg.sprite.Group()
grupo_torres = pg.sprite.Group()  # Grupo para torres

# criação dos botões
compra_torre = Botão(SCREEN_HEIGHT + 30, 100, imagem_compra_torre, True)
cancelar = Botão(SCREEN_HEIGHT+ 30, 200, imagem_cancelar_compra, True)
iniciar = Botão(SCREEN_HEIGHT+ 30, 650, imagem_iniciar, True)
avancar = Botão(SCREEN_HEIGHT+ 30, 550, imagem_avancar, False)
recomecar = Botão(590, 335, imagem_recomecar, True)


#variaveis
aguardando_posicao_torre = False  # Variável de controle para a colocação da torre
ultimo_spawn = pg.time.get_ticks()
inicio_jogo = False
game_over = False
resultado_jogo = 0 #-1 significa derrota e 1 significa vitoria
# Loop principal do jogo
run = True

while run:
    
    clock.tick(FPS)
    
    
    if game_over == False:
        #checando se o jogador perdeu
        if mundo.vida <= 0:
            game_over = True
            resultado_jogo = -1 #derrota
        if mundo.nivel > ULTIMO_NIVEL:
            game_over = True
            resultado_jogo = 1 #vitoria
            
        # Atualizações
        grupo_inimigos.update(mundo)
        grupo_torres.update()
        pg.display.update()
    
    # Desenhos
    mundo.draw(win)
    sidebar.draw(win)
    grupo_inimigos.draw(win)
    grupo_torres.draw(win)
    compra_torre.draw(win)
    escrita_texto(str(mundo.vida), fonte_texto, 'red', 10, 5)
    escrita_texto(str(mundo.dinheiro), fonte_texto, 'dark green', 10, 30)
    escrita_texto(str(mundo.nivel), fonte_texto, 'black', 10, 55)
    
    if game_over == False:
        #checando se o jogo começou
        if inicio_jogo == False:
            if iniciar.draw(win):
                inicio_jogo = True
        else:
            #opção de acelerar o jogo
            mundo.velocidade_nivel = 1
            if avancar.draw(win):
                mundo.velocidade_nivel = 3
            #spawnando inimigos
            if pg.time.get_ticks() - ultimo_spawn > (spawn_cooldown / mundo.velocidade_nivel):
                if mundo.inimigos_spawnados < len(mundo.lista_inimigos):
                    tipo_inimigo = mundo.lista_inimigos[mundo.inimigos_spawnados]
                    inimigo = Inimigo(tipo_inimigo, caminho, imagem_inimigo)
                    grupo_inimigos.add(inimigo)
                    mundo.inimigos_spawnados += 1
                    ultimo_spawn = pg.time.get_ticks()
        
        #checando se a wave acabou
        if mundo.checa_nivel_completo() == True:
            inicio_jogo = False
            mundo.nivel += 1
            ultimo_spawn = pg.time.get_ticks()
            mundo.reseta_nivel()
            mundo.processamento_inimigos()
            mundo.dinheiro += RECOMPENSA_NIVEL_COMPLETO
        
        if aguardando_posicao_torre == True:
            #mostrar torre no cursor:
            cursor_rect = torre_cursor.get_rect()
            cursor_pos = pg.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[0] <= SCREEN_HEIGHT and cursor_pos[1] <= SCREEN_WIDTH:
                win.blit(torre_cursor, cursor_rect)    
            if cancelar.draw(win):
                aguardando_posicao_torre = False
    else:
        pg.draw.rect(win, 'dark blue', (490, 260, 300, 200), border_radius = 30)
        if resultado_jogo == -1:
            escrita_texto('GAME OVER', fonte_texto_grande, 'black', 500, 275)
        elif resultado_jogo == 1:
            escrita_texto('VITÓRIA!', fonte_texto_grande, 'black', 525, 275)
        if recomecar.draw(win):
                game_over = False
                inicio_jogo = False
                aguardando_posicao_torre = False
                mundo = Mapa(imagem_mapa)
                ultimo_spawn = pg.time.get_ticks()
                mundo.reseta_nivel()
                mundo.processamento_inimigos()
                #limpando grupos
                grupo_inimigos.empty()
                grupo_torres.empty()
                
    # Verifica eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN: 
            mouse_pos = pg.mouse.get_pos()
            if event.button == 1 and compra_torre.rect.collidepoint(event.pos):  
                print('Clique no botão de compra de torre')
                # Define uma variável de controle para a criação da torre no próximo clique do botão direito
                aguardando_posicao_torre = True
            if mouse_pos[0] < SCREEN_HEIGHT and mouse_pos[1] < SCREEN_WIDTH:
                if event.button == 3 and aguardando_posicao_torre == True: 
                    print('Clique com o botão direito')
                    nova_torre = Torre(imagem_torre, event.pos) 
                    grupo_torres.add(nova_torre) 
                    aguardando_posicao_torre = False 

    pg.display.update()
pg.quit()
