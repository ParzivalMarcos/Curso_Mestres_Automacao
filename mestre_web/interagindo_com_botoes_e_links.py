from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Interacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        self.driver.get("https://cursoautomacao.netlify.app/index.html")
        sleep(4)


        # Clicar no link de login
        link_login = self.driver.find_element_by_xpath('//a[text()="Login"]')
        link_login.click()

        # Clicar no campo de email
        campo_email = self.driver.find_element_by_xpath('//input[@id="email"]')
        campo_email.click()

        # Digitar o email
        campo_email.send_keys('marcos@gmail.com')  # Método para inserir uma string digitando do teclado
        sleep(3)

        # Clicar no campo de senha
        campo_senha = self.driver.find_element_by_xpath('//input[@id="senha"]')
        campo_senha.click()

        # Digitar a senha
        campo_senha.send_keys('123456')
        sleep(3)

        # Clicar no botão 'Enviar' ou apertar Enter no teclado
        botao_enviar = self.driver.find_element_by_xpath('//button[text()="Enviar"]')
        botao_enviar.click()

interacao = Interacao()
interacao.Iniciar()