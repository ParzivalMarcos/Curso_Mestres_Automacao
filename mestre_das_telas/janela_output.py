import PySimpleGUI as sg

layout = [
    [sg.Text('Log de informações')],
    [sg.Output(size=(40, 5))],
    [sg.Input()], 
    [sg.Button('Salvar dados', key='salvar')],
]

janela = sg.Window('Opções de Valores', layout)

while True:
    evento, dados = janela.Read()
    if evento == 'salvar':
        print(evento)
        print(dados)
    
    if evento == sg.WIN_CLOSED:
        break

janela.close()