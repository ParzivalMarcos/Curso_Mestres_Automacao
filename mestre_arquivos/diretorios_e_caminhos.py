import os

# Navegando em diretorios

print(os.name)  # Exibe o nome do sistema operacional atual
print(os.listdir())  # Lista os arquivos do diretório atual
# os.chdir()  # Acessa diretorio
print(os.getcwd())  # Exibe o diretório atualmente em uso
print(os.sep) # Imprime o separador do sistema operacional onde está sendo executado
# Montando um caminho completo que funcoona em qualquer sistema operacional
print(os.path.join(os.getcwd() + os.sep + 'boleto.pdf'))
# Mesmo processo, porem entrando em sub pastas
print(os.path.join(os.getcwd() + os.sep + 'senhas' + os.sep + 'senhas.txt'))

caminho_boleto = os.path.join(os.getcwd() + os.sep + 'boleto.pdf')
print(os.path.dirname(caminho_boleto))
print(os.path.basename(caminho_boleto))

print(os.path.exists('teste.txt'))  # Verificar se diretorio existe
print(os.path.exists('boleto.pdf'))  # Verificar se diretorio existe