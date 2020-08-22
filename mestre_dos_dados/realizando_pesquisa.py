import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Criar um banco de dados SQLite3
Base = declarative_base()

class Artista(Base):
    
    __tablename__ = 'artista'
    artista_id = Column(Integer,Sequence('artista_id', start=1), primary_key=True)
    nome = Column(String)
    albuns = relationship('Album')  # relacionamento com tabela album
    


class Album(Base):

    __tablename__ = 'album'
    album_id = Column(Integer, Sequence('album_id', start=1), primary_key=True)
    titulo = Column(String)
    preco = Column(Numeric(10, 2)) # total de 10 numeros e 2 pontos depois da virgula
    artista_id = Column(Integer, ForeignKey('artista.artista_id'))  # Chave estrangeira de Artista
    estilo_id = Column(Integer, ForeignKey('estilo.estilo_id'))
    cancao = relationship('Cancao')  # relacionamento com tabela cancao


class Cancao(Base):

    __tablename__ = 'cancao'
    cancao_id = Column(Integer, Sequence('cancao_id', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey('album.album_id'))  # Chave estrangeira de Cancao


class EstiloMusical(Base):

    __tablename__ = 'estilo'
    estilo_id = Column(Integer, Sequence('estilo_id', start=1), primary_key=True)
    nome = Column(String)
    relationship('Album')


# Para criar um banco de dados
engine = create_engine('sqlite:///artistas2.db', echo=True)
Base.metadata.drop_all(bind=engine)  # recriando toda a tabela
Base.metadata.create_all(bind=engine)

Conexao = sessionmaker(bind=engine)
conexao = Conexao()
conexao: sessionmaker


novo_artista1 = Artista()
novo_artista1.nome = 'Artista 1'
novo_artista2 = Artista()
novo_artista2.nome = 'Artista 2'

novo_album1 = Album()
novo_album1.titulo = 'Album 1'
novo_album1.preco = 12.01
novo_album1.artista_id = 1
novo_album2 = Album()
novo_album2.titulo = 'Album 2'
novo_album2.preco = 13.50
novo_album2.artista_id = 2

conexao.add(novo_artista1)
conexao.add(novo_artista2)
conexao.add(novo_album1)
conexao.add(novo_album2)

conexao.commit()

# Usando query no banco de dados
for item in conexao.query(Artista).all():
    print(item.artista_id, item.nome)

# Quantidade de regisros em uma tabela
print(conexao.query(Album).count())

# Obter resultados ordenados em alguma condição
for item in conexao.query(Album).order_by(Album.artista_id):
    print(item.titulo, item.artista_id)

# Em ordem decrescente
for item in conexao.query(Album).order_by(desc(Album.artista_id)):
    print(item.titulo, item.artista_id)

# Obter o primeiro registro de uma tabela
artista = conexao.query(Artista).first()
print(artista.artista_id, artista.nome)

# Obter apenas uma quantidade de resultados especifica
for intem in conexao.query(Album).limit(1):
    print(item.album_id, item.titulo)

# Filtrar por propriedades especificas
# for item in conexao.query(Album).filter(Album.album_id == 2).\
#     filter(Album.preco == 14.07):
#     print(item.titulo, item.album_id, item.preco)

# Pesquisando por um item que contem uma string
# for item in conexao.query(Album).filter(Album.titulo.like('%top%')):
#   print(item.titulo, item.album_id)
