from csv import DictReader, DictWriter

def lendo_csv_sem_Dict():
    ## Forma antiga
    with open('csv_exemplo.csv') as arquivo:
        dados = arquivo.read()
        print(dados)

def lendo_arquivo_csv():
    with open('csv_exemplo.csv') as arquivo:
        leitor_csv = DictReader(arquivo)
        for linha in leitor_csv:
            print(linha['OrderId'] + ' ' + linha['First Name'])

def criando_csv():
    with open('computadores.csv', 'w', newline='', encoding='UTF-8') as arquivo:
        cabecalho = ['Marca', 'Preço', 'Ano de lançamento']
        escritor_de_csv = DictWriter(arquivo, fieldnames=cabecalho)
        escritor_de_csv.writeheader()
        escritor_de_csv.writerow({
            'Marca': 'Asus',
            'Preço': 3500.00,
            'Ano de lançamento': 2015

        })
        escritor_de_csv.writerow({
            'Marca': 'Dell',
            'Preço': 4000.00,
            'Ano de lançamento': 2017


        })
        escritor_de_csv.writerow({
            'Marca': 'Acer',
            'Preço': 4230.00,
            'Ano de lançamento': 2018

        })

def modificando_csv_existente():
    with open('csv_exemplo.csv', 'r') as arquivo_original:
        leitor_csv_original = DictReader(arquivo_original)
        pessoas = list(leitor_csv_original)

        with open('csv_exemploV2.csv', 'w', newline='') as novo_arquivo:
            # OrderId,First Name,Last Name,Gender,Country,Age,Date,ClientId
            cabecalho = ['OrderId', 'First Name', 'Last Name',
                         'Gender', 'Country', 'Age', 'Date', 'ClientId']
            escritor_csv = DictWriter(novo_arquivo, fieldnames=cabecalho)
            escritor_csv.writeheader()

            for linha in pessoas:
                escritor_csv.writerow({
                    'OrderId': 'Order Id ' + linha['OrderId'],
                    'First Name': linha['First Name'],
                    'Last Name': linha['Last Name'],
                    'Gender': linha['Gender'],
                    'Country': linha['Country'],
                    'Age': linha['Age'],
                    'Date': linha['Date'],
                    'ClientId': linha['ClientId'],
                })

if __name__ == "__main__":
    # lendo_arquivo_csv()
    # lendo_arquivo_csv()
    # criando_csv()
    modificando_csv_existente()
    