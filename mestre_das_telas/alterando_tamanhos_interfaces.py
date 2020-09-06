import PySimpleGUI as sg

sg.theme('DarkBlue3')


size_lower = (10, 1)
size_midle = (23, 1)
size_big = (26, 1)

layout = [
    [sg.Text('Nome', size=size_lower), sg.Text('E-mail', size=size_lower)],
    [sg.Input(size=size_lower), sg.Input(size=size_lower)],
    [sg.Text('Digite seu mês de aniversário', size=size_midle), 
     sg.Text('Qual site mais acessa?', size=size_midle)],
    [sg.Input(size=size_big), sg.Input(size=size_midle)],
    [sg.Text('Em qual aula estamos?', size=(18, 1))],
    [sg.Input(size=(20, 1))],
]

janela = sg.Window('Opções de valores', layout)

while True:
    evento, dados = janela.Read()


    if evento == sg.WINDOW_CLOSED:   
        break

janela.close()
