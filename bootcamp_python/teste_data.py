class NavegadorDeSites:
    def __init__(self, site, conteudo_a_buscar):
        self.site = site
        self.conteudo_a_buscar = conteudo_a_buscar

    
    def acessar_site(self):
        print(f"Navegando até o site {self.site} para extrair {self.conteudo_a_buscar}")


class NavegadorDeSitesDeComparacao(NavegadorDeSites):
    # def __init__(self, novo_parametro):
    #     super().__init__('amazon.com', 'Notebooks')
    #     self.novo_parametro = novo_parametro

    def buscador_de_preco(self, nome_do_produto, preco_maximo):
        print(f'Buscando informações sobre {nome_do_produto} com preço máximo de R${preco_maximo}')
        


def teste():
    teste = NavegadorDeSitesDeComparacao('amazon.com', 'Notebooks')
    teste.acessar_site()
    teste.buscador_de_preco('Notebook', 1500)
    
teste()