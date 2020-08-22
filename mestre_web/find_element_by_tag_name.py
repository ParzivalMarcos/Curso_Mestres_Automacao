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
        todos_os_botoes = self.driver.find_element_by_tag_name('button')
        if todos_os_botoes is not None:
            print('todos_os_botoes encontrado')
        elif todos_os_botoes is None:
            print('todos_os_botoes não encontrado')

curso = CursoAutomacao()
curso.Iniciar()