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

#Vamos inicializar o tamanho da tela, criando a varíavel, a função set mode recebe uma tupla, a qual a recebe comprimento e altura respectivamente
tela = pygame.display.set_mode((largura,altura))

#Podemos alterar o nome da janela que criamos ao rodar o código:
pygame.display.set_caption('Formas Geométricas!')

#Todo jogo se passa dentro de um loop, já que a cada ação o jogo precisará atualizar, portanto, ele se encontra dentro de um loop infinito
while True:
    #Criamos um for para dectetar alguma ação e um if para que caso ela seja feita, o jogo responda
    for evente in pygame.event.get():
        if evente.type == QUIT:
            pygame.quit()
            exit()
    #Adicionando formas geométricas:
        #rect = retangulo
        #Dentro da função rect, temos como parâmetro: onde, a tupla das cores em RGB e por ultimo outr tupla que recebe as coordenadas 'x' e 'y' no padrão do pygame e a largura e altura
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50))
        #No caso do circulo, as coordenadas x e y referem ao centro e o quarto parametro é o seu raio
    pygame.draw.circle(tela,(0,0,255),(300,300), 40)
        #Já nas linhas, temos a terceira e quarta tupla sendo os pontos inicial e final, e o ultimo valor sua expessura
    pygame.draw.line(tela,(255,255,0),(390,0),(390,600),5)
    #Comando usado para atualizar a tela a cada interação
    pygame.display.update()