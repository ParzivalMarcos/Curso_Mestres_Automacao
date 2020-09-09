import PySimpleGUI as sg
import sys


class Program:
    def __init__(self):
        self.usuarios = [
            {
                'usuario': 'marcos',
                'senha': '12345'        
            },
            {
                'usuario': 'admin',
                'senha': 'root'
            },       
        ]

    def main(self):
        sg.theme('DarkBlue3')
        screen_login = self.create_login_screen()

        while True:
            window, event, values = sg.read_all_windows()

            # Validações Tela de Login
            if window == screen_login and event == 'Login':
                user = values['user']
                passw = values['pass']

                for usuario in self.usuarios:
                    if usuario['usuario'] == user and usuario['senha'] == passw:
                        sg.popup('Login correto')
                        window.close()
                        sys.exit()
                    else:
                        window['acesso'].update(visible=True)
                    

            if window == screen_login and event in (sg.WIN_CLOSED, None, 'Sair'):
                window.close()
                sys.exit()


    def create_login_screen(self):
        layout = [
            [sg.Text('Digite seu usuário')],
            [sg.Input(key='user')],
            [sg.Text('Digite sua senha')],
            [sg.Input(key='pass', password_char='*')],

            [sg.Text(key='acesso', text='Login inválido', visible=False, text_color='red')],
            [sg.Button('Login'), sg.Button('Sair')]
        ]

        return sg.Window('Janela Login', layout, finalize=True)


program = Program()
program.main()
