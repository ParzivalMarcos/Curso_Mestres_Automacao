import PySimpleGUI as sg

tab1_cadastro = [
    [sg.Text('Digite seu nome')],
    [sg.Input()],
    [sg.Text('Digite seu estado')],
    [sg.Input()],
    [sg.Button('Salvar Cadastro')]
]

tab2_velocidade = [
    [sg.Text('Quantas buscas fazer por dia')],
    [sg.Slider(range=(1, 10), default_value=1)],
    [sg.Button('Salvar Velocidade')]
]


layout = [
    [sg.TabGroup([
        [sg.Tab('Cadastro', tab1_cadastro)],
        [sg.Tab('Velocidade', tab2_velocidade)]
    ])]
]

janela = sg.Window('Abas', layout)

while True:
    evento, valores = janela.Read()

    if evento == sg.WINDOW_CLOSED:
        break

janela.close()