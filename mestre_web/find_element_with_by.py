from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'/chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        ''' ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR '''
        self.driver.find_element(By.ID, 'Teste')
        self.driver.find_element(By.XPATH, '//div[@propriedade="teste"]')
        self.driver.find_element(By.LINK_TEXT, 'teste link')
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'teste link parcial')
        self.driver.find_element(By.NAME, 'nome')
        self.driver.find_element(By.TAG_NAME, 'h3 (exemplo)')
        self.driver.find_element(By.CLASS_NAME, 'nome da classe')
        self.driver.find_element(By.CSS_SELECTOR, 'div')


curso = CursoAutomacao()
curso.Iniciar()