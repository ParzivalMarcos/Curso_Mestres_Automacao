from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        self.SalvarScreenshot()

    def SalvarScreenshot(self):
        nome_arquivo = str(round(time.time() * 1000)) + '.png'
        nome_arquivo_com_diretorio = os.path.join('fotos', nome_arquivo)
        self.driver.save_screenshot(nome_arquivo_com_diretorio)

        time.sleep(2)

        self.driver.close()

automacao = Automacao()
automacao.Iniciar()