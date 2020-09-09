import PySimpleGUI as sg
import sys

# Layout do Menu
menu_tela_inicial = [
    ['Arquivo', ['Abrir', 'Salvar']],
    ['Editar', ['Alterar Imagem',['Alterar cor', 'Alterar Imagem'], 'Alterar Claridade']],
    ['Ajuda',['Versão']]
]

layout = [
    [sg.Menu(menu_tela_inicial)],
    [sg.Text('Bem vindo a este aplicativo!')],
    [sg.Output(size=(40,20))]
]

janela = sg.Window('Janela', layout)

while True:
    event, values = janela.Read()

    if event == sg.WIN_CLOSED:
        janela.close()
        sys.exit()
    if event == 'Alterar Claridade':
        print('Alterando a claridade')
