import PySimpleGUI as sg

sg.theme('DarkBlue3')

layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Digite sua idade')],
    [sg.Input(key='idade')],
    [sg.OK(), sg.Cancel('Cancelar'), sg.Button('Enviar Dados', key='enviar_dados'), 
     sg.Text(key='acesso', size=(20, 1))]
]

janela = sg.Window('Janela', layout)

while True:
    evento, valores = janela.Read()

    if evento == sg.WIN_CLOSED:
        break
    if evento == 'OK':
        if int(valores['idade']) >= 18:
            janela['acesso'].update('Acesso Concedido')
        else:
            janela['acesso'].update('Acesso negado')
            janela['enviar_dados'].update(disabled=True)

    if evento == 'Cancelar':
        break

janela.close()
