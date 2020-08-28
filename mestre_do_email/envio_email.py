import os
import smtplib
from email.message import EmailMessage
import imghdr
import time

def send_first_email():
    # Configuração login
    ENDERECO_EMAIL = 'marcosmarinhodev@gmail.com'
    SENHA = '********'

    # criando email
    msg = EmailMessage()
    msg['Subject'] = 'Teste Assunto email'
    msg['From'] = ENDERECO_EMAIL
    msg['To'] = 'marcolim977@gmail.com'
    msg.set_content('Olá, este email é um email de teste enviado de um Script Python')

    # fazendo o envio
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ENDERECO_EMAIL, SENHA)
        smtp.send_message(msg)


def send_email_with_image():
    # Login
    ENDERECO_EMAIL = 'marcosmarinhodev@gmail.com'
    SENHA = '********'

    # Criando Email
    msg = EmailMessage()
    msg['Subject'] = 'Enviando Anexos'
    msg['From'] = ENDERECO_EMAIL
    msg['To'] = 'marcolim977@gmail.com'
    msg.set_content('Segue em anexo!!')


    # Configurar o envio de imagens
    imagens = ['image_facebook.png', 'image_test.png']
    for imagem in imagens:
        with open(imagem, 'rb') as arquivo:
            dados = arquivo.read()
            extensao_imagem = imghdr.what(arquivo.name)
            nome_aruivo = arquivo.name
        msg.add_attachment(dados, maintype='image', subtype=extensao_imagem, filename=nome_aruivo)


    # Envio
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ENDERECO_EMAIL, SENHA)
        smtp.send_message(msg)


def send_email_attachment():
    # Login
    ENDERECO_EMAIL = 'marcosmarinhodev@gmail.com'
    SENHA = '********'

    # Configurando email
    msg = EmailMessage()
    msg['Subject'] = 'Enviando email em anexo'
    msg['From'] = ENDERECO_EMAIL
    msg['To'] = 'marcolim977@gmail.com'
    msg.set_content('Segue arquivos em anexo')


    # Anexar arquivo
    arquivos = ['arquivo_inicial.txt', 'boleto.pdf', 'computadores.csv']

    for arquivo in arquivos:
        with open(arquivo, 'rb') as a:
            dados = a.read()
            nome_arquivo = a.name

        # Configurando anexo
            # Enviando arquivos diferentes, como tipo:
            #  'maintype' e subtipo 'subtype' como valores padrões
        msg.add_attachment(dados, maintype='application', subtype='octet-stream', filename=nome_arquivo)

    # Enviando arquivo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ENDERECO_EMAIL, SENHA)
        smtp.send_message(msg)


def send_email_multiple_contacts():
    # Login
    ENDERECO_EMAIL = 'marcosmarinhodev@gmail.com'
    SENHA = '********'
    contatos = ['marcolim977@gmail.com', 'email2@gmail.com']

    # Configurando email
    msg = EmailMessage()
    msg['Subject'] = 'Enviando email para varios contatos'
    msg['From'] = ENDERECO_EMAIL
    msg['To'] = ', '.join(contatos)

    msg.set_content('Este é um email de teste, para multiplos contatos')

    # Fazendo envio
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ENDERECO_EMAIL, SENHA)
        smtp.send_message(msg)
        # time.sleep(180)  -> time para o envio de cada email

if __name__ == "__main__":
    # send_first_email()
    # test()
    # print('Finalizando')
    # send_email_with_image()
    # send_email_attachment()
    # send_email_multiple_contacts()
    pass