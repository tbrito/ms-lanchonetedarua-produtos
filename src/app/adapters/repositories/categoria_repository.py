from app.adapters.categoria_db import CategoriaDB
from app.adapters.categoria_mapper import CategoriaMapper
from app.adapters.internal.postgres_base import PostgresContext
from app.domain.ports.categoria_repository_port import CategoriaRepositoryPort

class CategoriaRepository(CategoriaRepositoryPort):
    def __init__(self, session_manager: PostgresContext):
        self._session = session_manager.session

    def get_by_id(self, categoria_id):
        categoria_db = self._session.query(CategoriaDB).get(categoria_id)
        return CategoriaMapper.map_categoria_db_to_entity(categoria_db)

    def get_all(self):
        categorias_entity = self._session.query(CategoriaDB).all()
        return CategoriaMapper.map_categorias_db_to_entities(categorias_entity)

    def add(self, categoria):
        categoria_db = CategoriaMapper.map_entity_to_categoria_db(categoria)
        self._session.add(categoria_db)
        self._session.commit()
        return CategoriaMapper.map_categoria_db_to_entity(categoria_db)

    def update(self, categoria_id, categoria_data):
        categoria = self._session.query(CategoriaDB).get(categoria_id)
        if categoria:
            categoria.nome = categoria_data.nome
            self._session.commit()

    def delete(self, categoria_id):
        categoria = self._session.query(CategoriaDB).get(categoria_id)
        if categoria:
            self._session.delete(categoria)
            self._session.commit()