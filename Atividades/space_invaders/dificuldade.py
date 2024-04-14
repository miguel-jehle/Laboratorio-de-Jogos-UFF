#AINDA NÃO FOI IMPLEMENTADO A DIFICULDADE!!!!! FAÇA UM PADRÃO E DEPOIS IMPLEMENTAR

#importar as bibliotecas e os outros módulos
from PPlay.window import*
from PPlay.sprite import*
import função
import jogar

def dificuldade() -> int:
    #Inicializando a janela
    janela = Window(537,457)
    janela.set_title("Space Invaders")

    #Inicializando o mouse
    mouse = janela.get_mouse()

     #Criando a variável de comandos
    comandos = Window.get_keyboard()

    #Desenhando a tela de menu com os botões falsos
    dif = Sprite("png/tela_dificuldade.png",1)
    dif.x = 0
    dif.y = 0

    #Inicializando os botôes
    facil = Sprite("png/facil.png",1)
    medio = Sprite("png/medio.png",1)
    dificil = Sprite("png/dificil.png",1)

    #Loop
    while True:
        #Desenhando o fundo com os botôes falsos, assim como no menu
        dif.draw()

        #Caso o mouse passe encima da área do botão falso, o verdadeiro aparecerá, com uma cor diferente do falso, dando o efeito solicitado pelo Esteban
        if mouse.is_over_area([163,132],[374,190]):
            função.posição(facil,163,132)
            if mouse.is_button_pressed(1):
                nivel = 1
                

        if mouse.is_over_area([163,229],[374,287]):
            função.posição(medio,163,229)
            if mouse.is_button_pressed(1):
                nivel = 2
                

        if mouse.is_over_area([163,325],[374,383]):
            função.posição(dificil,163,325)
            if mouse.is_button_pressed(1):
                nivel = 3
                
        
        janela.update()