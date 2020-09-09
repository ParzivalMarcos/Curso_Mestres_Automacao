import PySimpleGUI as sg
import time
import threading
from selenium import webdriver
import os


def OperacaoDemorada(janela, valores):
    driver = webdriver.Chrome(
        executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
    print(f"Navegando para o site {valores['site']}")
    driver.get(valores['site'])
    time.sleep(10)
    site_navegado = driver.current_url
    driver.quit()
    janela.write_event_value('automacao_web_finalizada', site_navegado)


def IniciarInterface():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Para qual site devemos navegar?')],
        [sg.Input(key='site')],
        [sg.Button('Iniciar'), sg.Button('Parar')],
    ]

    janela = sg.Window('Automatizando TUDO!', layout)

    thread_automacao_web = None
    while True:
        evento, valores = janela.Read()
        if evento in (sg.WIN_CLOSED, 'Exit'):
            break
        elif evento == 'Iniciar' and thread_automacao_web == None:
            # daemon = inicie em segundo plano
            thread_automacao_web = threading.Thread(target=OperacaoDemorada, 
                             args=(janela, valores,), daemon=True)  
            thread_automacao_web.start()
        elif evento == 'automacao_web_finalizada':
            thread_automacao_web.join()
            # Qualquer codigo abaixo, so sera executada após a finalização da thread
            print(valores['automacao_web_finalizada'])

    janela.close()


IniciarInterface()
