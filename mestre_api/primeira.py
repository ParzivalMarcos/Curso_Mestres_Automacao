import requests

resultado = requests.get('https://oslogin.googleapis.com/$discovery/rest?version=v1')

print(resultado.json())