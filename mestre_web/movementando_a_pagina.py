from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")

        # Movimentando até o final da página
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # Movimentando até o topo da página
        self.driver.execute_script('window.scrollTo(0, document.body.scrollTop);')
        sleep(5)

        self.driver.get('https://josephmark.ventures/')

        # Movimentando para a direita em Pixels
        self.driver.execute_script('window.scrollBy(1000, 0)')

        # Movementando para a esquerda em Pixels
        self.driver.execute_script('window.scrollBy(-1000, 0)')
        sleep(5)

        self.driver.get('https://coolors.co/')

        # Descendo em 500 pixels
        self.driver.execute_script('window.scollBy(0, 500')

        # Subindo em 500 pixels
        self.driver.execute_script('window.scrollBy(0, -500')


auto = Automacao()
auto.Iniciar()
        


automacao = Automacao()
automacao.Iniciar()