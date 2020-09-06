import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Slider(range=(1, 100), orientation='h', default_value=1)],
    [sg.Spin(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), initial_value=1)],
    [sg.Spin(values=('Iniciante', 'Intermediario', 'Avançado'), initial_value='Iniciante')],
    [sg.OK()],
    [sg.Combo(values=('Bronze', 'Prata', 'Ouro'), default_value='Bronze')],
    # [],

]

janela = sg.Window('Opções de Valores', layout)

while True:
    evento, dados = janela.Read()
    if evento == 'OK':
        print(dados)

    if evento == sg.WINDOW_CLOSED:
        break

janela.close()