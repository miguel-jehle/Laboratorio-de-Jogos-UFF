from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import menu

dificuldade = 1
control = Mouse()

def fim_de_jogo(score):
    janela = Window(537,457)
    
    teclado = janela.get_keyboard()
    
    fundo = GameImage("png/fundo_jogar.png")
    
    nome = input("Entre com o seu nome: ")
    
    # Abro o arquivo (leitura)
    arquivo = open('Pontuacao.txt', 'r')
    conteudo = arquivo.readlines()

    # Insiro o conteúdo
    conteudo.append(str(score) + " - " + nome + ".")
    arquivo.close()
    
    # Abre novamente o arquivo (escrita)
    arquivo = open('Pontuacao.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    
    while (True):
        #Desenho o fundo
        fundo.draw()

            
        janela.draw_text(("Você foi derrotado! Boa sorte na próxima!"), 40, 100, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para voltar ao menu"), 100, 200, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            menu.menu()
            
        # Atualizo o GameLoop
        janela.update()
        
def arquivo_to_codigo(file):
    arquivo = open(file)
    pontuacao = []
    for elemento in arquivo:
        temp = elemento.split(".")
        for i in temp:
            pontuacao.append(i)
    arquivo.close()
    return pontuacao
