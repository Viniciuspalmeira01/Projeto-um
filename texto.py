import PyPDF2 as Pdf
from banco_arquivos import db , Texto

#primeiro temos que abrir um arquivo pdf e ler este arquivo antes de colocá-lo no banco de dados
db.connect()
db.create_tables([Texto])


def ler_arquivopdf(caminho_pdf, numero_pagina = int):
    pdf_reader = Pdf.PdfReader(caminho_pdf)
    pages = pdf_reader.pages[numero_pagina]
    return pages.extract_text()


# Função para ler o conteúdo do arquivo de texto
def ler_arquivo_texto(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return file.read()

# Caminho do arquivo de texto que você quer inserir
caminho_arquivo = 'nota01.txt'
conteudo_arquivo = ler_arquivo_texto(caminho_arquivo)

# Inserir o conteúdo do arquivo de texto no banco de dados usando Peewee
texto_salvo = Texto.create(titulo=caminho_arquivo, texto=conteudo_arquivo)

lista_arquivos = Texto.select()
for x in lista_arquivos:
      print('Texto' , x.id , x.texto)