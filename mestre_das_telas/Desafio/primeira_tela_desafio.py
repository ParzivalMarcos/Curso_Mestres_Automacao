import PySimpleGUI as sg

# Definindo tema
sg.theme('DarkBlue3')

# Layout
layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input()],
    [sg.Text('Digite sua idade')],
    [sg.Input()],
    [sg.OK()],
]

# Window
janela = sg.Window("Desafio Primeira Janela", layout)

while True:
    event, valores = janela.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'OK':
        print(f'Seu nome é {valores[0]} e você tem {valores[1]} anos')

janela.close()