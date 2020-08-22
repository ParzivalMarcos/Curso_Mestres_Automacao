import sqlalchemy
from sqlalchemy import Integer, String, Sequence, create_engine, Column, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# valor_a_ser_alterado = conexao.query(Album).filter(Album.titulo == 'Winter Times').first()
# valor_a_ser_alterado.titulo = 'Winter Times 3000'

# conecao.commit()

# resltado = conexao.query(Album).filter(Album.titulo == 'Winter Times 3000')
# print(resltado.titulo, resltado.album_id)