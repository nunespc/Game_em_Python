from builtins import range

import pygame
from random import randint

pygame.init()
x = 380 # max = 560 min = 180
y = 100
pos_x = 526
pos_y = 1200
pos_y_a = 800
pos_y_b = 2000
time = 0
tempo_segundo = 0

velocidade_outros = 12

velocidade = 10
fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carro_novo.png')
policia = pygame.image.load('carro_novo4.png')
carro2 = pygame.image.load('carro_novo2.png')
carro3 = pygame.image.load('carro_novo3.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = 65, 50


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Primeiro jogo')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 545:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 200:
        x -= velocidade
    if pos_y <= -200:
        pos_y = 600

    if x + 80 > pos_x and y + 180 > pos_y:
        y = 1200
        texto = font.render('GAME OVER', True, (255, 255, 255), (50, 100, 50))


    if x - 80 < pos_x -300 and y + 180 > pos_y_a:
        y = 1200
        texto = font.render('GAME OVER', True, (255, 255, 255), (50, 100, 50))


    if x + 80 > pos_x - 136 and y + 180 > pos_y_b and x - 80 < pos_x and y + 180 > pos_y_b:
        y = 1200
        texto = font.render('GAME OVER', True, (255, 255, 255), (50, 100, 50))


    if pos_y <= -80:
        pos_y = randint(800, 1000)
    if pos_y_a <= -80:
        pos_y_a = randint(1200, 2000)
    if pos_y_b <= -80:
        pos_y_b = randint(2200, 3000)

    if time < 20:
        time += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: ' +str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        time = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_b -= velocidade_outros +10


    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(carro2, (pos_x - 300, pos_y_a))
    janela.blit(carro3, (pos_x - 136, pos_y_b))
    janela.blit(texto, pos_texto)
    pygame.display.update()
pygame.quit()