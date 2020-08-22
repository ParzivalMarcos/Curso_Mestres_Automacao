from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.site = input('Digite o site que deseja ir: ')

    def Iniciar(self):
        # self.driver.get('https://www.instagram.com')
        self.driver.get(f'https://{self.site}')

curso = CursoAutomacao()
curso.Iniciar()

