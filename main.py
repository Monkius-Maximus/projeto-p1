import pygame
import constants as c

pygame.init()

#clock
clock = pygame.time.Clock()

#setup da janela do jogo
win = pygame.display.set_mode((c.SCREEN_HEIGHT, c.SCREEN_WIDTH))
pygame.display.set_caption("Projeto P1")

#loop
run = True
while run:

    clock.tick(c.FPS)
    #loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
