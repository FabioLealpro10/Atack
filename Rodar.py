import time

import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

# Controle
# Movimentos => A D
# Atira => L

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura)) # tela

pygame.display.set_caption('ATACK') # nome

movimentar_obigeto = 400

atirar = False
bala = 550
destruir_vilao = False

local_vilao = randint(0, 780)
direita = True

vilao_atira = False
y_bala = 10
ja = False

pontos = 0
font = pygame.font.SysFont('arial',20,True,True)

vidas = 3

v_jogo = pygame.time.Clock()
while True:
    v_jogo.tick(300)
    tela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            exit()
        if evento.type == KEYDOWN:
            if pygame.key.get_pressed()[K_l] and not(atirar):
                atirar = True
                lacal_bala = movimentar_obigeto+8

    personagem = pygame.draw.rect(tela,(0,0,225),(movimentar_obigeto,550,20,20))
    txt_vidas = font.render(f'VIDAS: {vidas}',True,(250,250,250))
    kill = font.render(f'PONTOS: {pontos}', True, (250, 250, 250))
    tela.blit(txt_vidas,(0,300))
    tela.blit(kill,(680,300))
    if not(destruir_vilao):
        vilao = pygame.draw.rect(tela,(250,0,0),(local_vilao,0,20,20))
        if (local_vilao == 0) or (local_vilao==750) and not(vilao_atira):
            fogo = randint(1,749)
            vilao_atira = True
        if vilao_atira:
            if fogo == local_vilao:
                x_bala = fogo
                ja = True
        if ja:
            balav = pygame.draw.circle(tela, (0, 250, 0), (x_bala+10, y_bala), 20)
            y_bala += 1
            if balav.colliderect(personagem):
                vidas -= 1
                y_bala = 600
            if y_bala > 600:
                y_bala = 10
                vilao_atira = False
                ja = False

        if direita:
            if direita and local_vilao<780:
                local_vilao+=1
            else:
                direita = False
        else:
            if not(direita) and local_vilao>0:
                local_vilao-=1
            else:
                direita = True

    else:
        local_vilao = randint(0, 780)
        destruir_vilao = False


    if pygame.key.get_pressed()[K_a] and movimentar_obigeto>0:
        movimentar_obigeto-=2
    if pygame.key.get_pressed()[K_d] and movimentar_obigeto<780:
        movimentar_obigeto+=2

    if atirar and bala>0:
        fogo = pygame.draw.circle(tela,(250,250,250),(lacal_bala,bala),5)
        bala-=2
        if fogo.colliderect(vilao):
            destruir_vilao = True
            pontos+=1
            bala = 0


    else:
        atirar = False
        bala = 550

    pygame.display.update()