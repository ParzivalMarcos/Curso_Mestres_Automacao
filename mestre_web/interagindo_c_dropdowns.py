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
        pais_dropdown = self.driver.find_element_by_xpath("//select[@id='paisselect']")
        opcoes = Select(pais_dropdown)
        opcoes.select_by_index(2)  # Selecionando o Canada
        print('selecionando a opção do Canada')
        sleep(3)

        opcoes.select_by_value("brasil")
        print('Selecionando a opção do Brasil')
        sleep(3)

        opcoes.select_by_visible_text("Estados Unidos")
        print('Selecionando a opção dos Estados Unidos')
        sleep(3)

automacao = Automacao()
automacao.Iniciar()
