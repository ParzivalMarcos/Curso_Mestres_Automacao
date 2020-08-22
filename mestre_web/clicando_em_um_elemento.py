from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Clique:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)


    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/index.html')
        botao_dropdown = self.driver.find_element_by_id("dropdownMenuButton")
        botao_dropdown.click()
        # self.driver.execute_script("arguments[0].click()", botao_dropdown)  # Usando javascript, segunda forma

        lista_itens_dropdown = self.driver.find_elements_by_xpath("//*[@id='bootstrap4Dropdown']/a")
        for itens_dropdown in lista_itens_dropdown:
            print(itens_dropdown.text)


clique = Clique()
clique.Iniciar()