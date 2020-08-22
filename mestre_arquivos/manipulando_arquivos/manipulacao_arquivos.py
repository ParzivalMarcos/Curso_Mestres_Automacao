import os

"""
CRIAR E MODIFICAR ARQUIVOS

'r' -> Usado somente para ler algo
'w' -> Usado somentoe para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo
"""

valores_celulares = [850, 2230, 1500, 3500, 5000]
outros_valores_de_celulares = [245, 757]

planos_de_internet = ['Plano 50mb Básico', 
                      'Plano 100mb Médio', 'Plano 200mb Alto']


def sobrescrevendo_arquivo(arquivo):
    with open(arquivo, 'w') as arquivo:
        for valor in valores_celulares:
            arquivo.write(str(valor) + '\n')


def lendo_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha)


def adicionando_valores_em_arquivo(arquivo):
    with open(arquivo, 'a') as arquivo:
        for valor in outros_valores_de_celulares:
            arquivo.write(str(valor) + '\n')


def lendo_e_escrevendo(arquivo):
    with open(arquivo, 'r+') as arquivo:
        for linha in arquivo:
            print(linha)
        
        arquivo.write('\n' + 'Criando arquivos com Python')


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    nome_arquivo = 'Valores_celulares.txt'

    # sobrescrevendo_arquivo(nome_arquivo)
    # lendo_arquivo(nome_arquivo)
    # adicionando_valores_em_arquivo(nome_arquivo)
    lendo_e_escrevendo(nome_arquivo)

    print('** FIM **')
