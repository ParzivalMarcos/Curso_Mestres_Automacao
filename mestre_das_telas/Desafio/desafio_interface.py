import PySimpleGUI as sg


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

        self.licences = ['MAKDO29SLD-MAKDO29SLD-MAKDO29SLD-MAKDO29SLD',
                    'ASD123LASD-ASD123LASD-ASD123LASD-ASD123LASD',
                    'PADEL3R2KA-PADEL3R2KA-PADEL3R2KA-PADEL3R2KA']

    def main(self):

        screen_login, screen_licence = self.create_login_screen(), None

        while True:
            window, event, values = sg.read_all_windows()

            if window == screen_login and event == 'Login':
                for usuario in self.usuarios:
                    if usuario['usuario'] == values['user'] and usuario['senha'] == values['pass']:
                        screen_login.close()
                        screen_licence = self.create_license_screen()
                    else:
                        window['acesso'].update(visible=True)
                        pass

            if window == screen_licence and event == 'Validar Licensa':
                if values['licensa'] in self.licences:
                    sg.popup('Licensa Registrada com sucesso!!')
                else:
                    screen_licence['lic_invalida'].update(visible=True)

            if event in (sg.WIN_CLOSED, None, 'Sair'):
                break
        window.close()


    def create_login_screen(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Digite seu usuário')],
            [sg.Input(key='user')],
            [sg.Text('Digite sua senha')],
            [sg.Input(key='pass', password_char='*')],

            [sg.Text(key='acesso', text='Login inválido', visible=False, text_color='red')],
            [sg.Button('Login'), sg.Button('Sair')]
        ]
        return sg.Window('Janela Login', layout, finalize=True)


    def create_license_screen(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Favor digitar sua licença para continuar')],
            [sg.Input(key='licensa')],
            [sg.Button('Validar Licensa')],
            [sg.Text('Licença Inválida', key='lic_invalida', visible=False, text_color='red')]
        ]
        return sg.Window('Janela Licensa', layout, finalize=True)


program = Program()
program.main()
