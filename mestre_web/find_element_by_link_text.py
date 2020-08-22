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
        # link_pagina_desafios = self.driver.find_element_by_link_text('Desafios')
        link_pagina_desafios = self.driver.find_element_by_partial_link_text('fios')
        if link_pagina_desafios is not None:
            print('link_pagina_desafios encontrado')
        elif link_pagina_desafios is None:
            print('link_pagina_desafios não encontrado')

curso = CursoAutomacao()
curso.Iniciar()