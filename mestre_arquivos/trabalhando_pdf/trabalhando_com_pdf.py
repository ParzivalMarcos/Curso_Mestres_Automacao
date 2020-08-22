from pikepdf import Pdf
from pikepdf import Permissions
from pikepdf import Encryption


def copiando_um_pdf():
    with Pdf.open('PDF_Exemplo4.pdf') as pdf:
        pdf.save('novo.pdf')
        pdf.close()

def contando_numero_de_paginas():
    with Pdf.open('PDF_Exemplo2.pdf') as pdf:
        print(len(pdf.pages))
        pdf.close()

def removendo_paginas():
    with Pdf.open('PDF_Exemplo4.pdf') as pdf:
        del pdf.pages[2:4]  # Mantem a pagina 2 e exclui ate a pagina 4
        pdf.save('exemplo exclusão.pdf')

def separar_pdf_em_paginas_menores():
    with Pdf.open('PDF_Exemplo4.pdf') as pdf:
        print(len(pdf.pages))
        pdf_novo = Pdf.new()
        pdf_novo.pages.append(pdf.pages[0])
        pdf_novo.save('novo_pdf.pdf')

def juntar_merge_dois_pdfs():
    pdf = Pdf.new()
    fonte1 = Pdf.open('PDF_Exemplo2.pdf')
    fonte2 = Pdf.open('PDF_Exemplo3.pdf')

    pdf.pages.extend(fonte1.pages)
    pdf.pages.extend(fonte2.pages)

    pdf.save('pdf_combinado.pdf')
    fonte1.close()
    fonte2.close()
    pdf.close()


def protegendo_pdf_senha():
    with Pdf.open('PDF_Exemplo4.pdf') as pdf:
        restricoes = Permissions(extract=False, print_highres=False, modify_form=False)
        pdf.save('PDF_protegido_com_senha.pdf',
                 encryption=Encryption(user='usuario', allow=restricoes, owner='senha'))
        pdf.close()

if __name__ == "__main__":
    # novo_pdf = Pdf.new()

    # copiando_um_pdf()
    # contando_numero_de_paginas()
    # removendo_paginas()
    # separar_pdf_em_paginas_menores()
    # juntar_merge_dois_pdfs()
    # protegendo_pdf_senha()
    pass

