from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options
        )


    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.com')
        self.driver.maximize_window()  # maximizar janela
        self.driver.refresh()  # recarrega a pagina
        self.driver.get(self.driver.current_url)  # recarrega a pagina
        self.driver.back()  # volta a pagina anterior
        self.driver.forward()  # navega 1 vez para a frente
        print(self.driver.title)  # obtem o titulo da pagina
        print(self.driver.current_url)  # obtém a URL da pagina atual
        print(self.driver.page_source)  # obtem o código fonte da pagina atual
        self.driver.close() # fecha a janela atual
        self.driver.quit()  # fecha a sessão do driver e todas as abas
        print(self.driver.find_element_by_xpath('//a[@class="nacbar-brand"]').text) # obtem o texto dentro de um elemento
        print(self.driver.find_element_by_xpath('//a[@class="nacbar-brand"]').get_attribute('href')) # Pegando um atributo que esta dentro de uma tag

         

curso = CursoAutomacao()
# curso.Iniciar()
