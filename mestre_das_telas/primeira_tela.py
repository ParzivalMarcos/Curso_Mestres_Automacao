import PySimpleGUI as sg

# Tema
# Para ver todos os temas -> sg.theme_previewer
sg.theme('DarkBlue3')

# Layout
layout = [
    [sg.Text('Digite um número')],
    [sg.Input()],
    [sg.OK()],
]

# Janela
janela = sg.Window('Minha janela', layout)

# Leitura dos valores da tela
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break

    if evento == 'OK':
        print(valores)
        valores.clear
janela.close()
