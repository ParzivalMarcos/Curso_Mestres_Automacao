import PySimpleGUI as sg

# Tema
sg.theme('DarkBlue3')

layout = [
    [sg.Text('Digite um Site')],
    [sg.Input(key='campo_site')],
    [sg.Text('Fazer pesquisas em quais sites?')],
    [sg.Checkbox('Google', key='google'), sg.Checkbox('Yahoo', key='yahoo'), sg.Checkbox('Bing', key='bing')],
    [sg.Text('Pode rodar o programa de madrugada?')],
    [sg.Radio('Sim', group_id='horario_execucao', key='sim'), sg.Radio('Não', group_id='horario_execucao', key='nao')],
    [sg.Text('Quantas mensagens por dia')],
    [sg.Slider(range=(1, 10), default_value=1, orientation='h', key='mensagens_dia')],
    [sg.Button('Enviar dados')]
]

janela = sg.Window('CheckBoxes RadioButton Slider', layout=layout)

while True:
    evento, valores = janela.Read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Enviar dados':
        print(evento)
        print(valores)
janela.close()
