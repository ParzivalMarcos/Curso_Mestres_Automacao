import PySimpleGUI as sg
import sys

layout = [
    [sg.Input(key='caminho_arquivo')],
    [sg.FileBrowse('Carregar arquivos', 
                    target='caminho_arquivo', 
                    file_types=(("Arquivos de Texto", '*.txt'),
                                 ("Imagens PNG", '*.png'),
                                 ("Todos os arquivos", '.*'),)),
     sg.Button('Ler arquivo', key='ler_arquivo')],

]

janela = sg.Window('Janela', layout)

while True:
    evento, valores = janela.Read()

    if evento == sg.WINDOW_CLOSED:
        janela.close()
        sys.exit()

    if evento == 'ler_arquivo':
        caminho_arquivo = valores['caminho_arquivo']
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha)
    else:
        print(evento)