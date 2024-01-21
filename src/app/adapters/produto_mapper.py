from app.adapters.produto_db import ProdutoDB
from app.domain.entities.produto import Produto

class ProdutoMapper:

    @staticmethod
    def map_produtos_db_to_entities(produtos_entity):
        return [ProdutoMapper.map_produto_db_to_entity(produto_db) for produto_db in produtos_entity]

    @staticmethod
    def map_produto_db_to_entity(produto_db):
        if produto_db is None:
            return None
        return Produto(
            id=produto_db.id,
            nome=produto_db.nome,
            descricao=produto_db.descricao,
            categoria_id=produto_db.categoria_id,
            created_at=produto_db.created_at
        )
    
    @staticmethod
    def map_entity_to_produto_db(entity):
        if entity is None:
            return None
        return ProdutoDB(
            nome=entity.nome,
            categoria_id=entity.categoria_id,
            descricao=entity.descricao
        )