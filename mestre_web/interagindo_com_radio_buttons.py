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
        mac_radiobutton = self.driver.find_element_by_id('MacRadioButton')
        mac_radiobutton.click()

        if mac_radiobutton.is_selected():
            print('Radio button "mac" está selecionado')


curso = CursoAutomacao()
curso.Iniciar()