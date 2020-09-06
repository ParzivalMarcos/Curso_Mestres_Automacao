import PySimpleGUI as sg

layout = [
    [sg.Multiline(autoscroll=True, size=(40, 5))]
]

janela = sg.Window('Multi linha', layout)

while True:
    evento, dados = janela.Read()

    if evento == 'OK':
        print(dados)

    if evento == sg.WINDOW_CLOSED:
        break

janela.close()