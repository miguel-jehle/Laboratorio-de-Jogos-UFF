#Importando a biblioteca
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*

#Passando os parametros de tamanho da tela
tela = Window(800,800)

#Oque será escrito
tela.set_title("Exercício 2")

#Fazer com que fique mais tempo aberto
tela.delay(5000)

#Desenho da bola na tela
bola = Sprite("rosa.png")

#Coordenadas da bolinha
altura_bola = (tela.height/2)-(bola.height/2)
largura_bola = (tela.width/2) - (bola.width/2)

bola.set_position(largura_bola ,altura_bola)

#Velocidades
velx = 1
vely = 2


while True:
    #Movimentação da bola
    bola.x += velx
    bola.y += vely

    #Colisão
    if (bola.x + bola.width >= tela.width) or bola.x <= 0:
        velx = -(velx)
    if (bola.y + bola.height >= tela.height) or bola.y <= 0:
        vely = -(vely)

    tela.set_background_color([255,255,255])
    bola.draw()
    tela.update()
    