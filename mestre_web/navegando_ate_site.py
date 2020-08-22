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
        self.driver.get('https://www.instagram.com')

curso = CursoAutomacao()
curso.Iniciar()


# Baixando o webdriver e instalando automaticamente
# from webdriver_manager.chrome import ChromeDriverManager
# self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)