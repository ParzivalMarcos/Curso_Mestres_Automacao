from selenium import webdriver
import schedule
import time
import os
from mail_module import Emailer


chromedriver = os.getcwd() + os.sep + 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver)

# Acessando site para monitorar
driver.get('https://cursoautomacao.netlify.app/dinamico')


def verificar_mudancas():
    # driver.get(driver.current_url)
    preco = driver.find_element_by_xpath("//li[@id='BasicPlan']")

    if preco.text != 'R$ 9.99 / ano':
        mensagem = f'O preço foi alterado para {preco.text}'
        enviar_email(mensagem)

    elif preco.text == 'R$ 9.99 / ano':
        print('O preço continua o mesmo')


def enviar_email(mensagem):
    mail = Emailer(email_remetente='marcosmarinhodev@gmail.com',
                        senha_email='***')
    lista_contatos = ['marcolim977@gmail.com']    
    mail.conteudo_email('O preço foi ALTERADO!',lista_contatos, mensagem)
    mail.enviar(1)


schedule.every(2).minutes.do(verificar_mudancas)

while True:
    schedule.run_pending()
    time.sleep(1)

