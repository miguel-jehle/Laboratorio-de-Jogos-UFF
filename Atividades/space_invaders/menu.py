#importar as bibliotecas
from PPlay.window import*
from PPlay.sprite import*

#importando os outros módulos do código
import jogar
import dificuldade
import rank
import função
#import ranking  // está comentado pois o Esteban pediu para não mexermos ainda

def menu():
    #Inicializando a janela
    janela = Window(537,457)
    janela.set_title("Space Invaders")

    #Inicializando o mouse
    mouse = janela.get_mouse()

    #Desenhando a tela de menu com os botões falsos
    menu = Sprite("png/menu.png",1)
    menu.x = 0
    menu.y = 0

    #Inicializando botões
    b_jogar = Sprite("png/jogar.png",1)
    b_dif = Sprite("png/dificuldade.png", 1)
    b_rank = Sprite("png/ranking.png",1)
    b_sair = Sprite("png/sair.png",1)

    #Loop while
    while True:

        #Desenhando o menu
        menu.draw()

        #Se o mouse estiver sobre a area da imagem do falso botão, o botão interativo será desenhado e se ele for clicado, irá para a tela respectiva
        if mouse.is_over_area([163,157], [374,215]):
            função.posição(b_jogar,163,157)
            if (mouse.is_button_pressed(1)):
                jogar.jogar()

        if mouse.is_over_area([163,229], [374,287]):
            função.posição(b_dif, 163,229 )
            if (mouse.is_button_pressed(1)):
                dificuldade.dificuldade()

        if mouse.is_over_area([163,300], [374,358]):
            função.posição(b_rank,163,300)
            if (mouse.is_button_pressed(1)):
                rank.rank()
        
        if mouse.is_over_area([163,371], [374,429]):
            função.posição(b_sair,163,371)
            if(mouse.is_button_pressed(1)):
                janela.close()

        janela.update()