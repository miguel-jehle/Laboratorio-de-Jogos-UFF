#Este arquivo foi criado para conter todas as funções criadas ao longo de todos os outros arquivos, para tornar mais legivel e organizado os códigos!!!


#Importando
from PPlay.sprite import*
import random

#Desenhnado 
def posição (sprite, x, y):

    sprite.x = x
    sprite.y = y
    sprite.draw()

#Criando os tiros
def novo_tiro(nave, lista_de_tiros):

    tiro = Sprite("png/tiro.jpg", 5)
    tiro.set_sequence_time(0, 4, 300, True)

    tiro.x = nave.x + 2
    tiro.y = nave.y - tiro.height

    lista_de_tiros.append(tiro)

    return lista_de_tiros


def limitando_tiro(tiro, lista_de_tiros):
    
    if (tiro.y <= tiro.height * 3):
        tiro.update()

    if (tiro.y <= 0):
        lista_de_tiros.remove(tiro)


####################################################################################################

def criaProjInimigo(inimigo,listaProjeteisInimigos,cont):
    # Crio o projetil
    #cont+= 1
    if (cont % 3 == 0): projetilInimigo = Sprite("png/tiro - Copia.jpg")
    else: projetilInimigo = Sprite("png/tiro.jpg",1)
    projetilInimigo.x = inimigo[0].x + 50
    projetilInimigo.y = inimigo[0].y + projetilInimigo.height + 50
    if (random.random() < 0.3 and len(listaProjeteisInimigos)==0):
        listaProjeteisInimigos.append(projetilInimigo)
    
    #return cont

def tiroInimigo(janela,listaProjeteisInimigos,velProjetilInimigo):
    for i,projetilAlien in enumerate(listaProjeteisInimigos):
        projetilAlien.y += velProjetilInimigo*janela.delta_time()
        projetilAlien.draw()
        if (projetilAlien.y>janela.height):
            listaProjeteisInimigos.pop(i)

def delay(delay,linha):
    if linha==4:    
        delay = 40
    if linha==5:
        delay = 35
    if linha>=6:
        delay = 25
    return delay

def delayInimigo(delayInimigo,linha):
    if linha==4:
        delayInimigo = 100
    if linha==5:
        delayInimigo = 110
    if linha>=6:
         delayInimigo = 120
    return delayInimigo


#####################################################################################################

def hit(vidas,player,listaDeInimigos,listaProjeteisInimigos,score,cont,ver_especial):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(player) and cont%3 == 0):
            ver_especial = True
        if (projetil.collided(player) and cont % 3 != 0):
            listaProjeteisInimigos.pop(i)
            vidas-=1    
    return vidas, ver_especial

