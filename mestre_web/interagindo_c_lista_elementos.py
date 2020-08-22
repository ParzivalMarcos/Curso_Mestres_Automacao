from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options
        )


    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        lista_checboxes = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        self.driver.execute_script('arguments[0].click()', lista_checboxes[0])

        for checkbox in lista_checboxes:
            if not checkbox.is_selected():
                # checkbox.click()
                self.driver.execute_script('arguments[0].click()', checkbox)
            else:
                print('Checkbox ja foi selecionado')


automacao = Automacao()
automacao.Iniciar()