import os


def criando_lista_frutas(frutas):
    with open('frutas.txt', 'w') as arquivo:
        for fruta in frutas:
            arquivo.write(str(fruta) + '\n')


def mostrando_lista_frutas():
    with open('frutas.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha)


def adicionando_cores_nas_frutas(cores):
    with open('frutas.txt', 'a') as arquivo:
        for cor in cores:
            arquivo.write(str(cor) + '\n')


def top_liguagens(linguagens_programacao):
    with open('top 10 linguages.txt', 'w') as arquivo:
        for linguagem in linguagens_programacao:
            arquivo.write(str(linguagem) + '\n')


def criando_arquivos_a_partir_de_uma_lista(lista):
    for arquivo in lista:
        with open(f'{arquivo}', 'w') as arquivo:
            pass


if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))
    
    frutas = ['Maracuja', 'Uva', 'Laranja', 'Melancia', 'Morango']
    cores = ['Azul', 'Verde', 'Preto', 'Vermelho', 'Branco']
    linguagens_programacao = ['Python', 'Java Script', 'C', 'Java', 'Node.js']
    lista_arquivos = ['teste.txt', 'doc.pdf', 'planilha.xlsx']

    criando_lista_frutas(frutas)
    mostrando_lista_frutas()
    adicionando_cores_nas_frutas(cores)
    top_liguagens(linguagens_programacao)

    criando_arquivos_a_partir_de_uma_lista(lista_arquivos)
