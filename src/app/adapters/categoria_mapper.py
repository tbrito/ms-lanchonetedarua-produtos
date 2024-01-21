from app.adapters.categoria_db import CategoriaDB
from app.domain.entities.categoria import Categoria

class CategoriaMapper:

    @staticmethod
    def map_categorias_db_to_entities(categorias_entity):
        return [CategoriaMapper.map_categoria_db_to_entity(categoria_db) for categoria_db in categorias_entity]

    @staticmethod
    def map_categoria_db_to_entity(categoria_db):
        if categoria_db is None:
            return None
        return Categoria(
            id=categoria_db.id,
            nome=categoria_db.nome,
            created_at=categoria_db.created_at
        )
    
    @staticmethod
    def map_entity_to_categoria_db(entity):
        if entity is None:
            return None
        return CategoriaDB(
            nome=entity.nome,
        )