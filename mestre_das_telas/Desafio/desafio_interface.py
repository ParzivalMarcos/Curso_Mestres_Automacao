import PySimpleGUI as sg
import sys

sg.theme('DarkBlue3')

usuarios = [
    {
        'usuario': 'marcos',
        'senha': '12345'
    },
    {
        'usuario': 'admin',
        'senha': 'root'
    },
]

layout = [
    [sg.Text('Digite seu usuário')],
    [sg.Input(key='user')],
    [sg.Text('Digite sua senha')],
    [sg.Input(key='pass', password_char='*')],

    [sg.Text(key='acesso', text='Login inválido', visible=False, text_color='red')],
    [sg.Button('Login'), sg.Button('Sair')]
]

window = sg.Window('Janela Login', layout)

def exit_program():
    window.close()
    sys.exit()
    
while True:
    event, values = window.Read()
   
    if event == 'Login':
        user = values['user']
        passw = values['pass']

        for usuario in usuarios:
            if usuario['usuario'] == user and usuario['senha'] == passw:
                sg.popup('Login correto')
                exit_program()
            else:
                window['acesso'].update(visible=True)
            

    if event in (sg.WIN_CLOSED, None, 'Sair'):
        exit_program()

