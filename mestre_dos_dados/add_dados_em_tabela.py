import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar um banco de dados SQLite3
Base = declarative_base()

class Artista(Base):
    
    __tablename__ = 'artista'
    artista_id = Column(Integer, primary_key=True)
    nome = Column(String)  



# Para criar um banco de dados
engine = create_engine('sqlite:///artistas.db', echo=True)
Base.metadata.create_all(bind=engine)

# Criando uma conexão
Conexao = sessionmaker(bind=engine)
conexao = Conexao()
conexao: sessionmaker

# criar um novo artista
novo_artista = Artista()
novo_artista.artista_id = 1
novo_artista.nome = 'Artista 1'

# Add novo registro
conexao.add(novo_artista)

# Salvar a info no banco de dados
conexao.commit()

# Busca no banco de dados (query)
resultado = conexao.query(Artista).all()

for item in resultado:
    print(item.artista_id)
    print(item.nome)

novo_artista2 = Artista()
novo_artista2.artista_id = 2
novo_artista2.nome = 'Artista 2'

conexao.add(novo_artista2)
conexao.commit()