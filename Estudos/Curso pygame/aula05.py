#Importar a biblioteca do pygame
import pygame

#Importar o submódulo dentro da biblioteca pygame, importando todas as funções e constantes que ele possui
from pygame.locals import *

#Chamando a função responsável por fechar a janela
from sys import exit

#Importar a biblioteca random para gerar valores aleatórios
from random import randint

pygame.init()

#Inicializando as variáveis aqui para ficar mais didático
largura = 640
altura = 480

#Inicializando as variaveis de movimento
x = largura/2 #Vamos posicioná-lo no meio da tela
y = altura/2

#Vamos inicializar as variáveis do retangulo azul, para alterálas com o randint
w = randint(40,600)
z = randint(50,430)

#Vamos inicializar o tamanho da tela, criando a varíavel, a função set mode recebe uma tupla, a qual a recebe comprimento e altura respectivamente
tela = pygame.display.set_mode((largura,altura))

#Podemos alterar o nome da janela que criamos ao rodar o código:
pygame.display.set_caption('Colisões!')

#Para controlar a velocidade do movimento:
relogio = pygame.time.Clock()

#Todo jogo se passa dentro de um loop, já que a cada ação o jogo precisará atualizar, portanto, ele se encontra dentro de um loop infinito
while True:
    #Criamos um for para dectetar alguma ação e um if para que caso ela seja feita, o jogo responda
    for evente in pygame.event.get():
        if evente.type == QUIT:
            pygame.quit()
            exit()
    
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

    #Retângulo controlado
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    #Retângulo pra ser colidido
    ret_azul = pygame.draw.rect(tela,(0,0,255),(w,z,40,50))

    #Detectando colisões:
    #A função usada serve para detectar a colisão de algum retangulo com o vermelho, neste caso, passamos o azul como parametro
    if ret_vermelho.colliderect(ret_azul):
        w = randint(40,600)
        z =  randint(50,430)

    #Comando usado para atualizar a tela a cada interação
    pygame.display.update()