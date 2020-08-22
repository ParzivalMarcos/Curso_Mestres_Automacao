from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    
    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/')
        acesso1_checkbox = self.driver.find_element_by_id("acessoNivel1Checkbox")
        acesso2_checkbox = self.driver.find_element_by_id("acessoNivel2Checkbox")

        acesso1_checkbox.click()
        acesso2_checkbox.click()

        print(f"O acesso 1 checkbox foi selecionado? {acesso1_checkbox.is_selected()}")
        print(f"O acesso 2 checkbox foi selecionado? {acesso2_checkbox.is_selected()}")


curso = CursoAutomacao()
curso.Iniciar()