from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import pygame
import menu
import pontinhos

dificuldade = 1
control = Mouse()

def rank():
    janela = Window(537, 457)

    teclado = janela.get_keyboard()

    fundo = GameImage("png/fundo_jogar.png")

    # Organizo o arquivo txt em ordem decrescente
    pontuacao = pontinhos.arquivo_to_codigo('Pontuacao.txt')
    pontuacao.reverse()
    
        
    while (True):
         # Desenho o fundo
        fundo.draw()
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            menu.Menu()
        
        # Desenho a pontuacao
        altura = 150
        limite = 0
        for i,conteudo in enumerate(pontuacao):
            if i==0:
                continue
            if limite<5:
                janela.draw_text(str(i), 50, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                janela.draw_text(("."), (janela.width/2)-10, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                janela.draw_text(str(conteudo), (janela.width/2)-80, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
                altura+=45
                limite+=1
            
        # Desenho o texto titulo na janela
        janela.draw_text(("RANKING"), (janela.width / 2)-120, 50, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Defino o titulo do jogo
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()



