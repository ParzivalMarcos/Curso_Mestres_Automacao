from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Desafio:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    
    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        pagina_desafios = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        pagina_desafios.click()
        sleep(2)
        checkbox_conversivel = self.driver.find_element_by_id("conversivelcheckbox")
        checkbox_offroad = self.driver.find_element_by_id("offroadcheckbox")
        sleep(2)
        if not checkbox_conversivel.is_selected():
            self.driver.execute_script("arguments[0].click()", checkbox_conversivel)

        if not checkbox_offroad.is_selected():
            self.driver.execute_script("arguments[0].click()", checkbox_offroad)



desafio = Desafio()
desafio.Iniciar()