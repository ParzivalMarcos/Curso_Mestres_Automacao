from mail_module import Emailer

mail = Emailer(email_remetente='marcosmarinhodev@gmail.com', senha_email='******')

lista_contatos = ['email1@gmail.com', 'email2@gmail.com']

mail.conteudo_email(assunto='Teste Assunto',
                    lista_contatos=lista_contatos,
                    conteudo_email="Teste")
# mail.anexar_imagens()
# mail.anexar_imagens()
