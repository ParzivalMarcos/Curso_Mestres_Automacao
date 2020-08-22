from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Desafio:
    def __init__(self):    
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    
    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/desafios.html')

        for i in range(1, 4):
            botao = self.driver.find_element_by_xpath(f"//section/button[{i}]")
            if botao.is_enabled():
                print(f"{botao.text} está habilitado")
            else:
                print(f"{botao.text} não está habilitado")

desafio = Desafio()
desafio.Iniciar()