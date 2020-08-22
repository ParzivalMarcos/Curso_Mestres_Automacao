from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        botao_desafio = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        botao_desafio.click()

        dropdown_desafio6 = self.driver.find_element_by_id("paisesselect")
        opcoes = Select(dropdown_desafio6)
        
        opcoes.select_by_value('estadosunidos')
        print("Estados Unidos Selecionado")
        sleep(2)

        opcoes.select_by_value('africa')
        print("Africa Selecionada")
        sleep(2)

        opcoes.select_by_value('chille')
        print("Chile Selecionado")
        sleep(2)

        print('FIM!!')




automacao = Automacao()
automacao.Iniciar()
