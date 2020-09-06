import PySimpleGUI as sg
import sys

sg.theme('DarkBlue3')


# Colunas
coluna_esquerda = [
    [sg.Text('Insira seu usuário')],
    [sg.Input()],
    [sg.Text('Insira sua senha')],
    [sg.Input(password_char='*')]
]

coluna_meio = [
    [sg.Output(size=(40, 10))]
]

coluna_direita = [
    [sg.Text('Qual site automatizar?')],
    [sg.Checkbox('Opção 1'), sg.Checkbox('Opção 2')]
]

# Layout Principal
# justification='center'/'left'/'right'
# element_justification='center'/'left'/'right'

layout_principal = [
    [sg.Column(coluna_esquerda, element_justification='center'), 
     sg.Column(coluna_meio),
     sg.Column(coluna_direita)]
]

# Criar janela
janela = sg.Window('Janela Inicial', layout=layout_principal)

# Ler os encentos
while True:
    evento, valores = janela.Read()

    if evento in (sg.WINDOW_CLOSED, None):
        janela.close()
        sys.exit()
    else:
        print(evento)
