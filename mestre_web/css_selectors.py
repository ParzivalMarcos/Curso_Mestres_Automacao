from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        # Seletores CSS
        # tag (dig, section, button)
        # class (.nomeDaClass)
        # id (#nomeDOID)
        # self.driver.find_element_by_css_selector('#nomeDoId')
        self.driver.find_element_by_css_selector('input[class="form-check-input"]')  # maneira normal
        self.driver.find_element_by_css_selector('input[class^="form"]')  # inicia com
        self.driver.find_element_by_css_selector('input[class$="form-control"]')  # finaliza com
        self.driver.find_element_by_css_selector('input[class*="check"]')  # Contenha aquela palavra

        def desafio():
            # div[class='col-lg']
            # div[class*='boxed']
            # input[placeholder*='nome aqui']
            pass



curso = CursoAutomacao()
curso.Iniciar()