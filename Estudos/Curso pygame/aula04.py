#Importar a biblioteca do pygame
import pygame

#Importar o submódulo dentro da biblioteca pygame, importando todas as funções e constantes que ele possui
from pygame.locals import *

#Chamando a função responsável por fechar a janela
from sys import exit

pygame.init()

#Inicializando as variáveis aqui para ficar mais didático
largura = 640
altura = 480
#Inicializando as variaveis de movimento
x = largura/2 #Vamos posicioná-lo no meio da tela
y = altura/2
#Vamos inicializar o tamanho da tela, criando a varíavel, a função set mode recebe uma tupla, a qual a recebe comprimento e altura respectivamente
tela = pygame.display.set_mode((largura,altura))

#Podemos alterar o nome da janela que criamos ao rodar o código:
pygame.display.set_caption('Movimento controlado!')

#Para controlar a velocidade do movimento:
relogio = pygame.time.Clock()

#Todo jogo se passa dentro de um loop, já que a cada ação o jogo precisará atualizar, portanto, ele se encontra dentro de um loop infinito
while True:
    #Criamos um for para dectetar alguma ação e um if para que caso ela seja feita, o jogo responda
    for evente in pygame.event.get():
        if evente.type == QUIT:
            pygame.quit()
            exit()
        #OPÇÃO 1 (se manter pressionado n faz nada)
        #Criamos um if para caso o jogador pressione qualquer tecla, seja reconhecido pelo sistema
        # if evente.type == KEYDOWN:
        #     #Por exemplo: Se a tecla pressionada for 'a', faça:
        #     if evente.key == K_a:
        #         x -= 20
        #     if evente.key == K_d:
        #         x += 20
        #     if evente.key == K_w:
        #         y -= 20
        #     if evente.key == K_s:
        #         y += 20 

    #OPÇÃO 2
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_s]:
        y += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    
    #Vamos impedir que o retangulo suma
    if y > altura:
        y = 0
    if y < 0:
        y = altura
    if x > largura:
        x = 0
    if x < 0:
        x = altura

    #Movimento:
    #Para controlar a velocidade dos frames por segundo, quanto maior, mais rápido. O parametro é um int
    relogio.tick(60)

    #Comando usado para que o retangulo se mova e não se estique quando o y for incrementado, seu parametro é uma tupla RGB
    tela.fill((0,0,0))

     #Substituimos os valores das coordenadas pela varíavel, pois estes serão incrementados dando a ideia de movimento
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))

    #Comando usado para atualizar a tela a cada interação
    pygame.display.update()