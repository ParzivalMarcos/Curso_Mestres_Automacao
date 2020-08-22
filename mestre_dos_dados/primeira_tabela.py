import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey
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