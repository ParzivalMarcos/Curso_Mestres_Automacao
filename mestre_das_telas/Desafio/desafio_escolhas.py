import PySimpleGUI as sg

# Tema
sg.theme('BrownBlue')

# Layout
layout = [
    [sg.Text('Digite um site')],
    [sg.Input(key='site')],
    [sg.Text('Informe seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Fazer pesquinas em quais sites?')],
    [sg.Checkbox('Google', key='google'), 
     sg.Checkbox('Yahoo', key='yahoo'), 
     sg.Checkbox('Bing', key='bing')],
    [sg.Text('Informe quais periodos o programa deve rodar')],
    [sg.Radio('Manhã', key='periodo_manha', group_id='periodo'), 
     sg.Radio('Noite', key='periodo_noite', group_id='periodo')],
    [sg.Text('Rodar o programa de madrugada?')],
    [sg.Radio('Sim', key='madrugada_sim', group_id='madrugada'),
     sg.Radio('Nao', key='madrugada_nao', group_id='madrugada')],
    [sg.Text('Quantos dias o programa irá rodar')],
    [sg.Slider(range=(1, 31), default_value=14, orientation='h', key='dias')],
    [sg.Text('Quantas mensagens por dia?')],
    [sg.Slider(range=(1, 100), default_value=1, orientation='h', key='msg_dia')],
    [sg.Button('Enviar Dados'), sg.Button('Salvar Configurações', key='salvar')]
]


janela = sg.Window('Desafio', layout=layout)

while True:
    evento, dados = janela.Read()

    if evento == 'salvar':
        print('\nAs informações do programa foram salvas\n')
        print(dados)

    if evento == sg.WINDOW_CLOSED:
        break
    
janela.close()
    