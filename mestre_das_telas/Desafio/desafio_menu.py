import PySimpleGUI as sg
import sys

menu_tela = [
    ['File', ['New File', 'Save', 'Save-as']],
    ['Edit', ['Size',['Change Resolution', 'Change Height', 'Change Width']]],
    ['About', ['About author']]
]

layout = [
    [sg.Menu(menu_tela)],
    [sg.Text('Bem-Vindo a este aplicativo')],
    [sg.Output(size=(40,20))]
]

janela = sg.Window('Desafio Menu', layout)

while True:
    event, value = janela.Read()

    if event == sg.WINDOW_CLOSED:
        janela.close()
        sys.exit()
    if event == 'About author':
        print('Criado por Marcos em 2020')
