import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

from app.adapters.categoria_db import CategoriaDB

Base = declarative_base()

class ProdutoDB(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    categoria_id = Column(Integer, ForeignKey(CategoriaDB.id))
    categoria = relationship(CategoriaDB)
    descricao = Column(String())
    created_at = Column(DateTime(), default=datetime.datetime.now())