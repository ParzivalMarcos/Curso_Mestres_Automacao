import os

# os.mkdir('Musicas')
# os.makedirs('Musicas' + os.sep + 'Hip-Hop')

# Verificar se pasta existe
if not os.path.isdir('Musicas'):
    os.mkdir('Musicas')
else:
    print('Diretorio ja foi criado')