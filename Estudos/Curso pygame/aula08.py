#Importar a biblioteca do pygame
import pygame

#Importar o submódulo dentro da biblioteca pygame, importando todas as funções e constantes que ele possui
from pygame.locals import *

#Chamando a função responsável por fechar a janela
from sys import exit

#Importar a biblioteca random para gerar valores aleatórios
from random import randint

pygame.init()

#Função usada para se referir a porcentagem do volume da música
pygame.mixer.music.set_volume(0.01)

#Criando a variável da música usando a função tendo como parâmetro o nome do arquivo
musica_de_fundo = pygame.mixer.music.load('trilha_sonora/musica_fundo.wav')

#Ao passar -1 como parâmetro, a música repete em looping
pygame.mixer.music.play(-1)

#Fazendo o mesmo para o som de colisões
som_colisão = pygame.mixer.Sound('trilha_sonora/som_moeda.wav')

#Inicializando as variáveis aqui para ficar mais didático
largura = 640
altura = 480

#Inicializando as variaveis de movimento
x = largura//2 #Vamos posicioná-lo no meio da tela
y = altura//2

#Vamos inicializar as variáveis do retangulo azul, para alterálas com o randint
w = randint(40,600)
z = randint(50,430)

#Usamos o comando abaixo para inicializar a fonte, com os parametros de fonte, tamanho, negrito e italico
fonte = pygame.font.SysFont('arial',40,True,False)
cont = 0

#Vamos inicializar o tamanho da tela, criando a varíavel, a função set mode recebe uma tupla, a qual a recebe comprimento e altura respectivamente
tela = pygame.display.set_mode((largura,altura))

#Podemos alterar o nome da janela que criamos ao rodar o código:
pygame.display.set_caption('Cobrinha pt1')

#Para controlar a velocidade do movimento:
relogio = pygame.time.Clock()

#Temos que criar ela fora do loop para n ser apagada a cada volta
lista_cobra = []

#Criamos o comprimeto da cobra que será usado de parâmetro
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for coordenadas in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(coordenadas[0],coordenadas[1],20,20))

#Todo jogo se passa dentro de um loop, já que a cada ação o jogo precisará atualizar, portanto, ele se encontra dentro de um loop infinito
while True:

    #Criando a mensagem
    mensagem = f'Pontos: {cont}'
    
    #Aqui usamos essa função para unir mensagem e fonte, onde temos como parametros a mensagem, pixelado ou não, e cor
    texto = fonte.render(mensagem, True, (0,0,0) )

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
    tela.fill((255,255,255))

    #Retângulo controlado
    cobra = pygame.draw.rect(tela, (0,255,0), (x,y,20,20))

    #Retângulo pra ser colidido
    maca = pygame.draw.rect(tela,(255,0,0),(w,z,20,20))

    #Detectando colisões:
    #A função usada serve para detectar a colisão de algum retangulo com o vermelho, neste caso, passamos o azul como parametro
    if cobra.colliderect(maca):
        w = randint(40,600)
        z =  randint(50,430)
        cont += 1
        som_colisão.play()
        comprimento_inicial += 1

    #Vamos criar uma lista para armazenar as posições da cobra
    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)

    #Vamos criar essa matriz para armazenar as coordenadas juntas
    lista_cobra.append(lista_cabeca)

    #Chamamos a função criada para aumentar 
    aumenta_cobra(lista_cobra)

    #Colocando na tela a mensagem desejada e as coordenadas de onde
    tela.blit(texto,(450,40))

    #Comando usado para atualizar a tela a cada interação
    pygame.display.update()