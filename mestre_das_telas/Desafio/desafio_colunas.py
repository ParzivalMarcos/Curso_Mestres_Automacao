import PySimpleGUI as sg

apresentacao_cluna1 = 'Olá estou na coluna 1'
apresentacao_cluna2 = 'Olá estou na coluna 2'
apresentacao_cluna3 = 'Olá estou na coluna 3'

coluna_1 = [
    [sg.Text(apresentacao_cluna1)],
    [sg.OK()],
    [sg.Text(apresentacao_cluna1)],
    [sg.OK()]
]

coluna_2 = [
    [sg.Text(apresentacao_cluna2)],
    [sg.OK()],
    [sg.Text(apresentacao_cluna2)],
    [sg.OK()]
]

coluna_3 = [
    [sg.Text(apresentacao_cluna3)],
    [sg.OK()]
]

layout = [
    [sg.Column(coluna_1), sg.Column(coluna_2), sg.Column(coluna_3)]
]


janela = sg.Window('Desafio', layout)

while True:
    evento, dados = janela.Read()

    if evento == sg.WINDOW_CLOSED:
        break

janela.close()