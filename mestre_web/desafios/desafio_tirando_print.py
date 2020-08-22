from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep, time
import os


class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=chrome_options
        )


    def Iniciar(self):
        self.AcessaSite('https://www.facebook.com')
        self.SalvarScreenshot('facebook')

        self.AcessaSite('https://www.instagram.com')
        self.SalvarScreenshot('instagram')

        self.AcessaSite('https://www.google.com')
        self.SalvarScreenshot('google')




    def SalvarScreenshot(self, nome):
        nome_arquivo = str(round(time() * 1000)) + f'_{nome}' + '.png'
        diretorio = os.path.join('fotos', nome_arquivo)
        self.driver.save_screenshot(diretorio)


    def AcessaSite(self, site):
        self.driver.get(site)
        sleep(1)


auto = Automacao()
auto.Iniciar()
auto.driver.close()
