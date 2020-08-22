import json
from pathlib import Path

def criando_arquivo_json():
    carros = [
        {"Marca":"Nissan", "Preço":45.000, "Cor":"Azul"},
        {"Marca":"Ford", "Preço":75.000, "Cor":"Preto"},
        {"Marca":"BMW", "Preço":145.000, "Cor":"Cinza"}
    ]

    carros_json = json.dumps(carros)
    Path('carros.json').write_text(carros_json)


def lendo_arquivos_json():
    arquivo_carro_json = Path('carros.json').read_text()
    arquivo_json = json.loads(arquivo_carro_json)
    print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço']))
    print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço']))

if __name__ == "__main__":
    criando_arquivo_json()
    lendo_arquivos_json()
