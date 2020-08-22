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
        # navbar-expand-md navbar-light
        navbar = self.driver.find_element_by_class_name('navbar.navbar-expand-md.navbar-light')
        if navbar is not None:
            print('navbar encontrado')
        elif navbar is None:
            print('navbar não encontrado')

curso = CursoAutomacao()
curso.Iniciar()