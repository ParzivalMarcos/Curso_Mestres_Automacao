import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Button('Botão comum')],
    [sg.Cancel()],
    [sg.Ok()],
    [sg.Yes()],
    [sg.No()],
    [sg.Quit()],
    [sg.Exit()],
    [sg.CalendarButton('Escolha uma data', target='alvo1'), 
        sg.InputText(key='alvo1', size=(20, 1))],
    [sg.ColorChooserButton('Escolha uma cor', target='alvo2'), 
        sg.Input(key='alvo2', size=(30, 1))],
    [sg.FileBrowse('Escolha um arquivo', target='alvo3'),
        sg.Input(key='alvo3', size=(30,1))],
    [sg.FilesBrowse('Escolher arquivos', target='alvo4'),
        sg.Input(key='alvo4', size=(30, 10))],
    [sg.FolderBrowse('Escolher uma pasta', target='alvo5'),
        sg.Input(key='alvo5', size=(30, 10))],
]

janela = sg.Window('Janela', layout=layout)

while True:
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        janela.close()
        break
    else:
        print(event, values)