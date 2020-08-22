from csv import DictReader, DictWriter

def criando_arquivo_csv():
    with open('pessoas.csv', 'w', newline='', encoding='UTF-8') as arquivo:
        cabecalho = ['nome', 'idade', 'altura']

        arquivo_csv = DictWriter(arquivo, fieldnames=cabecalho)
        arquivo_csv.writeheader()
        arquivo_csv.writerow({
            'nome': 'Mark',
            'idade': 25,
            'altura': 170
        })
        arquivo_csv.writerow({
            'nome': 'Carol',
            'idade': 19,
            'altura': 160
        })
        arquivo_csv.writerow({
            'nome': 'Robert',
            'idade': 65,
            'altura': 175
        })

def modificando_arquivo_csv():
    with open('pessoas.csv', 'r') as arquivo:
        arquivo_original = DictReader(arquivo)
        lista_pessoas = list(arquivo_original)

        with open('pessoasV2.csv', 'w', newline='', encoding='UTF-8') as novo_arquivo:
            cabecalho = ['nome', 'idade', 'altura']
            arquivo_csv = DictWriter(novo_arquivo, fieldnames=cabecalho)
            arquivo_csv.writeheader()

            for linha in lista_pessoas:
                arquivo_csv.writerow({
                    'nome': linha['nome'],
                    'idade': linha['idade'],
                    'altura': linha['altura'] + 'cm'
                })


if __name__ == '__main__':
    criando_arquivo_csv()
    modificando_arquivo_csv()