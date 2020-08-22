from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class Desafio:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=ptBR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options)

    
    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/index.html")

        # Encontrar e clicar no campo 'Desafios'
        link_desafios = self.driver.find_element_by_xpath('//a[text()="Desafios"]')
        link_desafios.click()

        # Digitar nome no campo de Desafios 2
        campo_desafio2 = self.driver.find_element_by_xpath('//input[@id="dadosusuario"]')
        campo_desafio2.send_keys("Marcos")
        sleep(2)

        # Clicar no botão "Clique aqui"
        botao_desafio2 = self.driver.find_element_by_xpath('//button[@id="desafio2"]')
        botao_desafio2.click()

        # Digitar novamente o nome no campo de texto
        campo_escondido = self.driver.find_element_by_xpath('//input[@id="escondido"]')
        campo_escondido.send_keys("Marcos")
        sleep(2)

        # Clicar no botão "Validar"
        botao_validar = self.driver.find_element_by_xpath('//button[@id="validarDesafio2"]')
        # sleep(2)
        botao_validar.click()

desafio = Desafio()
desafio.Iniciar()