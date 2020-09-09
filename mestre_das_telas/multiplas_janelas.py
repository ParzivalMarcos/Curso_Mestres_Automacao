import PySimpleGUI as sg
import sys


def criar_janela_1():
    layout = [
        [sg.Text('Registre seu nome na competição')],
        [sg.Button('Abrir segunda janela'), sg.Button('Sair')]
    ]
    return sg.Window('Janela', layout, finalize=True)

def criar_janela_2():
    layout = [
        [sg.Text('Bem vindo a segunda tela')],
        [sg.OK()]
    ]
    return sg.Window('Janela 2', layout, finalize=True)


janela1, janela2 = criar_janela_1(), None

while True:
    janela, evento, valores = sg.read_all_windows()

    if evento in (sg.WIN_CLOSED, None):
        janela.close()
        sys.exit()
    
    if janela == janela1 and evento == "Abrir segunda janela":
        janela2 = criar_janela_2()
        # janela1.hide  --> Manter janela em sefundo plano
        # janela1.un_hide  --> Retornar janela de segundo plano
        janela1.close()
    
    if janela == janela2 and evento == 'OK':
        sg.popup('Botão OK foi pressionado')