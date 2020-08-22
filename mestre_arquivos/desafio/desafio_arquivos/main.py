import os

def exibindo_todos_os_arquivos():
    print('Exibindo todos os arquivos da pasta'.upper())
    print(f'{os.listdir()}\n')


def exibindo_arquivos_pasta_atual():
    print('Monte e exiba o caminho(path) dos 3 arquivos da pasta atual'.upper())
    extensoes = ['xlsx', 'txt', 'pdf']
    for arquivo in os.listdir():
        for extensao in extensoes:
            if arquivo.endswith(extensao):
                print(f'{os.path.join(os.getcwd() + os.sep + arquivo)}\n')                    


def exibindo_arquivos_sub_pasta():
    print('Monte e exiba o caminho(path) dos 3 arquivos que estão dentro das sub-pastas'.upper())
    for arquivo in os.listdir('desafios_texto'):
        print(f'{os.path.join(os.getcwd() + os.sep + arquivo)}\n')


def navegando_nas_pastas():
    print('\nNavegando até a pasta desafios texto'.upper())
    os.chdir('desafios_texto')
    print(os.getcwd())

    print('\nNavegando novamente para a pasta desafios arquivos'.upper())
    os.chdir('..')
    print(os.getcwd())

    print('\nNavegando para o diretorio pai da pasta arquivos'.upper())
    os.chdir('..')
    print(os.getcwd())


if __name__ == "__main__":
    exibindo_todos_os_arquivos()
    exibindo_arquivos_pasta_atual()
    exibindo_arquivos_sub_pasta()
    navegando_nas_pastas()
        