from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

from time import sleep
import random

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options
        )
        # self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(
            driver= self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
                ]
        )
        # self.implicitly_wait(10)

    
    def Iniciar(self):
        print('** Iniciando Programa **\n')
        self.driver.get('https://cursoautomacao.netlify.app/')
        # self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//xpath')))
        self.MarcarRadioButton()
        self.DigitarComentario()
        self.DefinirNivelDeAcesso()
        print('\n## Encerrando programa ##')


    def MarcarRadioButton(self):
        # Encontrar os radio buttons
        windows_radio_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='WindowsRadioButton']"))) 

        mac_radio_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='MacRadioButton']"))
        )

        linux_radio_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='LinuxRadioButton']"))
        )

        # Perguntar ao usuario qual campo deseja marcar
        while True:
            opcao = input(str("Qual opção deve ser selecionada? -> ")).lower()
            if opcao == 'windows':
                self.driver.execute_script('arguments[0].click()', windows_radio_button)
                break
            elif opcao == 'mac':
                self.driver.execute_script('arguments[0].click()', mac_radio_button)
                break
            elif opcao == 'linux':
                self.driver.execute_script('arguments[0].click()', linux_radio_button)
                break
            else:
                print('\nOpção inválida, tente novamente\n')


    def DigitarComentario(self):
        # Encontrar o parágrafo
        campo_paragrafo = self.driver.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/textarea')

        # Solicitar para o usuario o comentario
        comentario = input(str('Qual comentário gostaria de deixar?\n-> '))

        # Digitar o comentario no campo paragrafo
        self.Digitando_como_uma_pessoa(comentario, campo_paragrafo)


    def Digitando_como_uma_pessoa(self, texto, elemento):
            for letra in texto:
                elemento.send_keys(letra)
                sleep(random.randint(1, 5) / 30)


    def DefinirNivelDeAcesso(self):
        # Solicitar ao usuario quais niveis de acesso.
        niveis = input(str('Quais níveis devem ser liberados?\n(Digite os valores separados por vírgula)\n-> ')).split(',')

        
        for nivel in niveis:
            acesso = self.wait.until(expected_conditions.
            element_to_be_clickable((
                By.XPATH, f'//*[@id="acessoNivel{nivel}Checkbox"]'
            )))
            self.driver.execute_script('arguments[0].click()', acesso)
            sleep(2)


auto = Automacao()
auto.Iniciar()