#Importando a biblioteca
from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*

#Passando os parametros de tamanho da tela
tela = Window(1200,600)
tela.set_title("Exercício 4")

#Criando o controle
controle = tela.get_keyboard()

#Fazer com que fique mais tempo aberto
tela.delay(5000)

#Criação dos pads
pad1 = Sprite("raquete_pong.png")
pad1.x = pad1.width * 2
pad1.y = tela.height/2 - pad1.height/2

pad2 = Sprite("raquete_pong.png")
pad2.x = (tela.width) - (pad2.width * 3)
pad2.y = (tela.height/2) - (pad2.height/2)

#Desenho da bola na tela
bola = Sprite("rosa.png")


#Coordenadas da bolinha
altura_bola = (tela.height/2)-(bola.height/2)
largura_bola = (tela.width/2) - (bola.width/2)

bola.set_position(largura_bola ,altura_bola)

#Velocidades
velx = -300
vely = 400
velp = 320
velIA = 380

#Pontuação 
esquerda = 0
direita = 0
Colidiu = False

while True:
    #Movimentação da bola
    bola.x += velx * tela.delta_time()
    bola.y += vely * tela.delta_time()

    #Movimento da IA induzida ao erro(Não muito burra nem muito impossível)
    if (bola.x >= tela.width/2 and bola.y >= tela.height/2 and vely > 0):
        pad2.y += velIA * tela.delta_time()
    if (bola.x >= tela.width/2 and bola.y <= tela.height/2 and vely < 0):
        pad2.y -= velIA * tela.delta_time()

    #Controles
    if (controle.key_pressed("w")):
        pad1.y -= velp * tela.delta_time()
    elif (controle.key_pressed("s")):
        pad1.y += velp * tela.delta_time()

    if (controle.key_pressed("up")):
        pad2.y -= velp * tela.delta_time()
    elif (controle.key_pressed("down")):
        pad2.y += velp * tela.delta_time()

    #Impedir que os pads saiam da tela
    if (pad1.y <= 0):
        pad1.y = 0
    if (pad1.y + pad1.height >= tela.height):
        pad1.y = tela.height - pad1.height
    if (pad2.y <= 0):
        pad2.y = 0
    if (pad2.y + pad2.height >= tela.height):
        pad2.y = tela.height - pad2.height

    if(bola.y <= 0):
        bola.y = 0
        vely *= (-1)
    if(bola.y + bola.height >= tela.height):
        bola.y = tela.height - bola.height
        vely *= (-1)

    #Define a pontuação
    if (bola.x + bola.width >= tela.width):
        esquerda += 1
        velx *= -1
        bola.x = tela.width/2 - bola.width/2
        bola.y = tela.width/2 - bola.height/2

    if (bola.x <= 0):
        direita += 1
        velx *= -1
        bola.x = tela.width/2 - tela.height/2
        bola.y = tela.width/2 - tela.height/2
        
    if Colidiu and controle.key_pressed("space"):
        velx = 100
        vely = 200
        Colidiu = False

    if (pad1.collided(bola)):
        velx *= -1
        bola.x  = pad1.x + pad1.width
    if(pad2.collided(bola)):
        velx *= -1
        bola.x = pad2.x - bola.width

    tela.set_background_color([255,255,255])

    tela.draw_text("{} esquerdo x {} direita" .format(esquerda, direita),tela.width/2 -120, 30, 20, (0,0,0), "Arial", True, False)

    pad1.draw()
    pad2.draw()
    bola.draw()
    tela.update()
    