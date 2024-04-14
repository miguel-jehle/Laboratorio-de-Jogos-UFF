#Importando 
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
import função
import menu
import inimigo
import rank
import pontinhos

#Criando a função principal que será chamada no código do menu e virá para a tela do jogo.
def jogar() -> int:

    #Criando a janela
    janela = Window(537,457)
    janela.set_title("Space Invaders")

    fundo = Sprite("png/fundo_jogar.png",1)
    fundo.x = 0
    fundo.y = 0


    #Criando a variável de comandos
    comandos = Window.get_keyboard()

    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()

    #Criação da nave
    nave = Sprite("png/player.png")
    nave.x = (janela.width - janela.height) / 2
    nave.y = janela.height - nave.height
    nave.set_sequence_time(0, 2, 200, True)
    naveInvencible = Sprite("png/invencivel.png",1)

    velnave = 200

    #CRIAÇÃO DOS DISPAROS
    disparos = []
    disparosinimigos = []
    cont = 0
    recarga = 1
    veltiro = 400

    #CRIAÇÃO DOS MONSTROS
    matrizDeInimigos = []
    linha = 4
    coluna = 8
    movimentoInimigo = 60
    movimentoInimigoBase = movimentoInimigo

    # Crio a pontuaçao que os aliens dão e o delay de invencibilidade
    score = 0
    TomeiDano=False
    ver_especial = False
    vida = 3
    delay = 0 
    delayInvencible = 0
    delayInimigo = 100
    estatico = 0
    
    #Loop
    while True:

        fundo.draw()

        # Conto o fps
        clock.tick(FPS)

        #Se o esc for apertado, retorna para o menu
        if comandos.key_pressed('esc'):
            menu.menu()
        
    #COMANDOS RELACIONADOS A NAVE:

        #Movimentação
        if (comandos.key_pressed("A")):
            nave.x -= velnave * janela.delta_time()
        if (comandos.key_pressed("D")):
            nave.x += velnave * janela.delta_time()

        #Limitando a nave na tela
        if (nave.x <= 0):
            nave.x = 0
        if (nave.x >= janela.width - nave.width):
            nave.x = janela.width - nave.width
    
    # Crio os inimigos
        if (len(matrizDeInimigos)==0):
            inimigo.cria_monstro(linha,coluna,matrizDeInimigos)

        # Recrio a matriz apos matar todos os aliens
        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:    
            matrizDeInimigos.clear()
            movimentoInimigo=movimentoInimigoBase
            nave.x= janela.width/2-nave.width/2
            delayInvencible=180
            #if linha<5:
            linha+=1
            movimentoInimigo*=1.03
            movimentoInimigoBase*=1.03
            inimigo.cria_monstro(linha,coluna,matrizDeInimigos)

    # Faço o movimento dos inimigos
        movimentoInimigo = inimigo.moveInimigos(janela, matrizDeInimigos, movimentoInimigo)

    #COMANDOS RELACIONADOS A TIROS:

        recarga += janela.delta_time()

        #ativar o tiro assim que o espaço for pressionado e respeitando o tempo de recarga
        if (comandos.key_pressed("space")) and (recarga >= 1/2) and (estatico <= 0):
            disparos = função.novo_tiro(nave,disparos)
            recarga = 0

        #desenha, controla e limita o disparo
        if (disparos != []):
            for d in disparos:
                d.draw()
                d.y -= veltiro * janela.delta_time()
                d = função.limitando_tiro(d, disparos)

        if (delayInimigo==0):
            for i in matrizDeInimigos:
                cont+= 1
                for j in i:
                    função.criaProjInimigo(j,disparosinimigos,cont)
            delayInimigo = função.delayInimigo(delayInimigo,linha)

        função.tiroInimigo(janela,disparosinimigos,veltiro)

        # Verifico se alguem tomou hit
        vidasAntes = vida
        score, movimentoInimigo = inimigo.kill(disparos,matrizDeInimigos,score,linha,movimentoInimigo)
        if (vida>0 and delayInvencible==0):
            for i in matrizDeInimigos:
                vida, ver_especial = função.hit(vida, nave, i, disparosinimigos,score,cont,ver_especial)
                if vida != vidasAntes:
                    TomeiDano=True
        if TomeiDano:
            nave.x= janela.width/2-nave.width/2
            delayInvencible=180
            TomeiDano=False

        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        if delayInvencible>0:
            delayInvencible-=1
            naveInvencible.x = nave.x
            naveInvencible.y = nave.y
            naveInvencible.draw()
        else:
            nave.draw()

        if ver_especial:
            posx = nave.x
            posy = nave.y
            estatico = 120
            ver_especial = False

        if estatico > 0:
            estatico -= 1
            nave.x = posx
            nave.y = posy

            

        
        # Perco o jogo
        if (vida <= 0):
            pontinhos.fim_de_jogo(score)
        for i in range(len(matrizDeInimigos)-1,-1,-1):
            for j in matrizDeInimigos[i]:
                if j[0].collided(nave) or j[0].y>=nave.y - nave.height:
                    pontinhos.fim_de_jogo(score)
        

        # Desenho os inimigos
        inimigo.draw(matrizDeInimigos)

         # Desenho a pontuação
        janela.draw_text(("Score: "), janela.width-130, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), janela.width-50, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])

        # Desenho a vida
        janela.draw_text(("Vidas: "), 0, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(vida), 75, 0, size=24, font_name="Arial", bold=True,color=[255, 0, 0])
        
        janela.update()