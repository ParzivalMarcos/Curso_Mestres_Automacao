import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import base
from models.db_models import Album, Artista
# from models.datab_model import cut


def iniciar():
    conexao = configurar_banco_de_dados()
    criar_artista(conexao=conexao, nome='Marcos')
    criar_album(conexao=conexao, titulo='Dev Aprender', preco=50.50, artista_id=1)

def criar_artista(conexao, nome):
    novo_artista = Artista()
    novo_artista.nome = nome
    conexao.add(novo_artista)
    conexao.commit()

def criar_album(conexao, titulo, preco, artista_id):
    novo_album = Album()
    novo_album.titulo = titulo
    novo_album.preco = preco
    novo_album.artista_id = artista_id
    conexao.add(novo_album)
    conexao.commit()

def buscar_todos_albuns(conexao):
    for item in conexao.query(Album).all():
        print(item.titulo, item.preco)

def configurar_banco_de_dados():
    engine = create_engine('sqlite:///artistas.db', echo=True)
    base.metadata.drop_all(bind=engine)  # Dropa estrutura atual
    base.metadata.create_all(bind=engine)  # Cria tabelas baseados na

    Conexao = sessionmaker(bind=engine)
    conexao = Conexao()
    return conexao


if __name__ == '__main__':
    iniciar()
