from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        checkbox_windows = self.driver.find_element_by_xpath("//input[@id='WindowsRadioButton']")
        checkbox_windows.click()

        checkbox_windows.send_keys(Keys.DOWN)

automacao = Automacao()
automacao.Iniciar()