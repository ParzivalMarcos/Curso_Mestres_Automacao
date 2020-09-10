import PySimpleGUI as sg
from time import sleep


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

        screen_login, screen_licence, screen_config = self.create_login_screen(), None, None

        while True:
            window, event, values = sg.read_all_windows()

            if window == screen_login and event == 'Login':
                for usuario in self.usuarios:
                    if usuario['usuario'] == values['user'] and usuario['senha'] == values['pass']:
                        screen_licence = self.create_license_screen()
                        screen_login.close()
                    else:
                        window['acesso'].update(visible=True)

            if window == screen_licence and event == 'Validar Licensa':
                if values['licensa'] in self.licences:
                    sg.popup('Licensa Registrada com sucesso!!')
                    screen_licence.close()
                    screen_config = self.create_config_screen()
                else:
                    screen_licence['lic_invalida'].update(visible=True)
            
            if window == screen_config and event == 'Iniciar':
                print('Iniciando Automação...')
                sleep(3)
                print('Encerrando...')
                break                

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


    def create_config_screen(self):
        sg.theme('Reddit')

        layout_config_initial = [
            [sg.Text('Qual site gostaria de automatizar?')],
            [sg.Radio('Site 1', group_id='site', key='site_1_ligado'),
             sg.Radio('Site 2', group_id='site', key='site_2_ligado'),
             sg.Radio('Site 3', group_id='site', key='site_3_ligado')],

            [sg.Checkbox('Opção 1'),
             sg.Checkbox('Opção 2'),
             sg.Checkbox('Opção 3')],

            [sg.Text('Quantas postagens devem ser veitas nestes sites?')],
            [sg.Slider(range=(1, 100), default_value=1, orientation='h', key='qtd_postagems')]
        ]

        layout_config_messages = [
            [sg.Multiline(default_text='Digite a mensagem a ser enviada', size=(32, 6), key='mensgem')],

            [sg.Text('Quantas mensagens por dia?')],
            [sg.Combo(values=(2, 4, 6, 8, 10, 12, 14, 16, 18, 20), default_value='2')],

            [sg.Text('Qual é o perfil da sua conta?')],
            [sg.Combo(values=('Bronze', 'Prata', 'Ouro'), default_value='Bronze')],

            [sg.Text('Quantos sites processar por dia?')],
            [sg.Spin(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), initial_value=1)]
        ]

        layout = [
            [sg.Frame('Configurações Iniciais', layout_config_initial),
             sg.Frame('Configurações de Mensagens', layout_config_messages)],
            [sg.Button('Iniciar')]
        ]
        return sg.Window('Janela Configurações', layout, finalize=True)



program = Program()
program.main()
