import random

class Dado:
    def __init__(self):
        pass


    def rodar_dado(self):
        valor_dado = random.randint(1, 6)
        print(f'Valor do dado: {valor_dado}')
        self.continuar()

    def continuar(self):
        continuar = input('Deseja rodar o dado novamente? (s/n)')
        if continuar == 's':
            dado.rodar_dado()
        elif continuar == 'n':
            dado.sair()
        else:
            print('Valor inválido !!')
            self.continuar()


    def sair(self):
        print('Obrigado por jogar, e até uma próxima')


dado = Dado()
dado.rodar_dado()

