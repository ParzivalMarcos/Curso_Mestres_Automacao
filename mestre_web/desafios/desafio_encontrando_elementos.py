from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class elementos:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        paragrafo = self.driver.find_element_by_xpath("//*[contains(text(), 'Parágrafo')]")
        drop_or_classic = self.driver.find_element_by_xpath("//*[contains(text(), 'Dropdown') or contains(text(), 'Clássico')]")
        elem_and_btn = self.driver.find_element_by_xpath("//*[contains(text(), 'Elementos') and contains(text(), 'botões')]")
        abrir_nova_janela = self.driver.find_element_by_xpath("//*[contains(text(), 'Exemplo abrir Nova Janela')]")
        id_botao = self.driver.find_element_by_xpath("//*[@id='divBotao']")
        class_form = self.driver.find_element_by_xpath("//*[@class='form-control']")