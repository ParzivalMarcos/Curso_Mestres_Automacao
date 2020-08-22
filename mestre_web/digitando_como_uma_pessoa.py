from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

class Automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque pulvinar pretium accumsan. Phasellus pharetra dui quis magna iaculis congue. Nullam ullamcorper molestie cursus. Donec vulputate augue a quam egestas efficitur. Curabitur non venenatis erat, eu molestie lectus. Sed sed nisl quis felis tempor mollis. Fusce vel felis mauris. Donec ornare ut massa nec scelerisque. Vestibulum sit amet vestibulum ex. Cras a elit lacinia, vehicula nisl at, ullamcorper nibh. Ut cursus fermentum augue, ut mollis nulla faucibus at. In hac habitasse platea dictumst. Mauris id diam sit amet quam vulputate feugiat. Etiam placerat rhoncus purus, vel efficitur magna ultrices a. Donec scelerisque sollicitudin dapibus. Nullam velit nisl, consequat id ullamcorper finibus, ullamcorper ut nulla."

    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        campo_paragrafo = self.driver.find_element_by_xpath(
            "//textarea[@placeholder='digite seu texto aqui']")
        self.digite_como_uma_pessoa(self.texto, campo_paragrafo)


    def digite_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)


auto = Automacao()
auto.Iniciar()