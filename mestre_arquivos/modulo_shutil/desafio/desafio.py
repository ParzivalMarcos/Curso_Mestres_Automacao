import shutil
import os

BASE_DIR = os.getcwd()

# Copie o arquivo nomes.txt para a pasta 'Arquivos2010'
shutil.copy(BASE_DIR + os.sep + 'nomes.txt',
            BASE_DIR + os.sep + 'Arquivos2010')

# Mova o arquivo inscricoes.pdf para a pasta 'Documentação'
shutil.move(BASE_DIR + os.sep + 'inscricoes.pdf',
            BASE_DIR + os.sep + 'Documentacao')

# Faça uma copia da pasta 'Arquivos2010' e tudo que estiver contido nela para uma
# novapasta chamada 'BackupArquivos2010'
shutil.copytree(BASE_DIR + os.sep + 'Arquivos2010',
                BASE_DIR + os.sep + 'BackupArquivos2010')

# Compacte todo o conteúdo da pasta 'Documentacao' no formato zip
shutil.make_archive('Documentacao', 'zip', BASE_DIR + os.sep + 'Documentacao')

# Mova o arquivo compactado para dentro da pasta 'Backup'
shutil.move(BASE_DIR + os.sep + 'Documentacao.zip', BASE_DIR + os.sep + 'Backup')

# Exclua o diretório 'Arquivos2010' e 'Documentacao' e seus conteúdos
shutil.rmtree(BASE_DIR + os.sep + 'Arquivos2010')
shutil.rmtree(BASE_DIR + os.sep + 'Documentacao')

# Compacte o diretorio inteiro, para um arquivo chamado 'BackupArquivosPython.zip'
shutil.make_archive('BackupArquivosPython', 'zip', BASE_DIR)

