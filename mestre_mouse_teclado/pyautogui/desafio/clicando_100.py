from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import os
from time import sleep

class DesafioClick():
    def __init__(self):
        chrome_option = Options()
        chrome_option.add_argument('--lang=pt-BR')
        chrome_option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_option)
        self.driver.implicitly_wait(10)

    
    def Iniciar(self):
        self.acessa_site()
        sleep(1)
        self.clicar_100_vezes()

    def acessa_site(self):
        self.driver.get('https://cpstest.org/100-seconds.php')
        self.driver.maximize_window()
        self.driver.execute_script('window.scrollBy(0,400)')

    def clicar_100_vezes(self):
        pyautogui.click(x=843, y=634, clicks=100, interval=0.1, duration=3)
        print('*** Finalizado ***')
        sleep(5)
        self.driver.close()


class CriarPasta():
    
    def __init__(self):
        pass

    
    def Iniciar(self):
        # 716,460
        pyautogui.click(x=728, y=460, clicks=1, duration=2, button='right')
        
        # 950,823
        pyautogui.moveTo(x=853, y=863, duration=1.5)
        pyautogui.move(xOffset=200, yOffset=0, duration=1)
        sleep(2)

        # 1078,395
        pyautogui.click(x=1084, y=423, clicks=1, duration=2, button='left')

        # 716,460
        pyautogui.click(x=728, y=460, duration=2)


if __name__ == '__main__':

    desafio = DesafioClick()
    desafio.Iniciar()

    sleep(1)

    pasta = CriarPasta()
    pasta.Iniciar()
