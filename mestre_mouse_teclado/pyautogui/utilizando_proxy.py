from selenium import webdriver
import time
import os

# 91.224.98.206 36301
PROXY = '91.224.98.206:36301'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')
caminho_webdriver = 'caminho/do/chromedriver.exe'

driver = webdriver.Chrome(
    executable_path=caminho_webdriver, options=chrome_options)

driver.get('https://www.google.com.br')
