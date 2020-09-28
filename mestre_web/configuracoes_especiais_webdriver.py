from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Fonte de Switches
# https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc
# https://peter.sh/experiments/chromium-command-line-switches/
arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']

'''
Common arguments
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o indioma de inicialização
--incognito # Usar em modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano (janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
'''

for argument in arguments:
    chrome_options.add_argument(argument)

caminho_padrao_para_download = 'C://Storage//Desktop'

# Lista de opções experimentais
# https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc

chrome_options.add_experimental_option("prefs", {
    # Atualiza diretorio de download
    'download.default_directory': caminho_padrao_para_download,

    # Atualizar o local padrão
    'download.directory_upgrade': True,

    # Impedir que o navegador pergunte se realmente deseja fazer o download
    'downliad.prompt_for_download': False,
    
    # Desabilita notificações
    "profile.default_content_setting_values.notifications": 2, 
    
    # Permitir multiplos downloads
    "profile.default_content_setting_values.automatic_downloads": 1,
})

driver = webdriver.Chrome(
    executable_path=r'./chromedriver.exe', options=chrome_options
)
driver.get('https://www.google.com.br')
