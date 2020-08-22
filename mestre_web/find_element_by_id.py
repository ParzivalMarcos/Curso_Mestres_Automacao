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
        botao_dropdown = self.driver.find_element_by_id('dropdownMenuButton')
        if botao_dropdown is not None:
            print('Botão dropdown encontrado')
        elif botao_dropdown is None:
            print('Botão dropdown não encontrado')

curso = CursoAutomacao()
curso.Iniciar()