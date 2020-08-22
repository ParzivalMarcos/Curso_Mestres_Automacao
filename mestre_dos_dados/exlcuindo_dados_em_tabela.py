import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# album_a_ser_excuido = conexao.query(Album).filter(Album.titulo == 'Sunny Mornig').first()
# conexao.delete(album_a_ser_excuido)
# conexao.commit()