from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options
        )

    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        botao_desafio = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        botao_desafio.click()

        lista_checkboxes_carros = self.driver.find_elements_by_xpath("//input[@id='conversivelcheckbox']")
        for indice in range(0, len(lista_checkboxes_carros)):
            if (indice == 2 or indice == 4 or indice >= 5):
                self.driver.execute_script('arguments[0].click()', lista_checkboxes_carros[indice])

        campo_cidade = self.driver.find_elements_by_xpath("//input[@class='form-control cidadesinput']")
        [campo.send_keys("São Paulo") for campo in campo_cidade]

automacao = Automacao()
automacao.Iniciar()