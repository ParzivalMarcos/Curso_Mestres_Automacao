import random
from time import sleep

respostas = [
        'Faça o que quiser! ',
        'Você realmente deseja fazer isto?',
        'Se assim o quer, faça, e faça já',
        'Não me importo com você',
        'Melhor não!!',
        'Não sei',
        'Que ótima idéia !!'
        ]

continuar = True
def retorna_resposta(respostas):
    return random.choice(respostas)

def perguntando_ao_usuario():
    input("Pergunte o que deseja fazer: ")
    print('Pensando...')
    sleep(5)
    print(retorna_resposta(respostas))


while continuar:
    perguntando_ao_usuario()
    sleep(2)
    try:
        refazer = int(input('Deseja fazer outra pergunta?\n[1] SIM\n[2] NAO\n-> '))
        if refazer == 2:
            continuar = False
        elif refazer < 1 or refazer > 2:
            print('Resposta invalida !!')
            perguntando_ao_usuario()
    except ValueError:
        print('Valor digitado invalido !!')
