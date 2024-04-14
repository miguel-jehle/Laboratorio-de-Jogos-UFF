from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*

#Função para criar inimigos
def cria_monstro(linha,coluna,matrizDeInimigos):    
    for i in range(linha):
        linhas = []
        for j in range(coluna):
            if linha<6:
                if i==0:
                    monstro = Sprite("png/monstro3.png",1)
                elif i==linha-1:
                    monstro = Sprite("png/monstro1.png",1)
                else:
                    monstro = Sprite("png/monstro2.png",1)
            if linha>=6:
                if i==0:
                    monstro = Sprite("png/monstro3.png",1)
                elif i==linha-2:
                    monstro = Sprite("png/monstro1.png",1)
                elif i==linha-1:
                    inimigoBonus = Sprite("png/monstrobonus.png",1)
                    inimigoBonus.x = 50
                    inimigoBonus.y = 50
                    break
                else:
                    monstro = Sprite("png/monstrobonus.png",1)
            monstro.x = 40 * j
            monstro.y = 30 * i
            linhas.append((monstro,1))
        matrizDeInimigos.append(linhas)
    
    if linha>=6:
        return inimigoBonus
    
#Função de desenhar
def draw(matrizDeInimigos):
    for linha in range(len(matrizDeInimigos)-1,-1,-1):
        for monstro in matrizDeInimigos[linha]:
            monstro[0].draw()


#Função que move os inimigos
def moveInimigos(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j[0].x += movimentoInimigo*janela.delta_time()
            if ((j[0].x >= janela.width - j[0].width - 5) or (j[0].x<-5)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j[0].x += movimentoInimigo*janela.delta_time()
                j[0].y += 30
    return movimentoInimigo

def kill(listaProjeteis,matrizDeInimigos,score,linha,movimentoInimigo):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                    if (projetil.collided(inimigo[0])):
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                score+=30
                            elif k==linha-1:
                                score+=10
                            else:
                                score+=20
                            movimentoInimigo*=1.01
    return score,movimentoInimigo