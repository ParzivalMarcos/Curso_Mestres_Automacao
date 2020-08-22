from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', 
            options=chrome_options)

    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/')
        # //tag[@atributo='valor']
        # Procurando elementos pelo texto
        self.driver.find_element_by_xpath()
        self.driver.find_element_by_xpath('//*[contains(text(), "Exemplo")]')
        self.driver.find_element_by_xpath('//*[contains(text(), "Exemplo") or contains(text(), "Dropdown")]')
        self.driver.find_element_by_xpath('//*[contains(text(), "Exemplo") and contains(text(), "Checkbox")]')
        self.driver.find_element_by_xpath('//*[starts-with(text(), "Elemento")]')  # Primeira palava de um texto

        # Procurando elementos pela classe
        self.driver.find_element_by_xpath('//*[starts-with(@class, "btn")]')

        # Procurando elementos exatamente pelo texo
        self.driver.find_element_by_xpath('//*[text()="Dropdown Clássico"]')
        self.driver.find_element_by_xpath('//h4[text()="Exemplo Checkbox"]') # Especificando a tag

        # Procurando elementos pelo id
        self.driver.find_element_by_xpath('//button[@id="dropdownMenuButton"]')
        self.driver.find_element_by_xpath('//section[@class="jumbotron"]') # Exatamente pela classe

        self.driver.find_element_by_xpath('//thead[@class="thead-dark"]//th[3]') # Encontrando elementos filhos
        

curso = CursoAutomacao()
curso.Iniciar()