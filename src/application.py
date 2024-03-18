import os

from dotenv import load_dotenv
from flask import Blueprint, Flask
from flask_restx import Api
from app.adapters.internal.postgres_base import PostgresContext
from app.adapters.repositories.categoria_repository import CategoriaRepository
from app.adapters.repositories.produto_repository import ProdutoRepository
from app.domain.services.categoria_service import CategoriaService
from app.domain.services.produto_service import ProdutoService

from app.entrypoints.produto_resource import api as produtos_ns
from app.entrypoints.categorias_resource import api as categorias_ns

from container_di import ContainerDI

def configure_inject() -> None:
    database_uri = os.getenv('DATABASE_URI')
    session_manager = PostgresContext("postgresql://postgres:QE1muGg0fwsepsH@lanchonetedaruadb.c16om6u44j69.us-east-1.rds.amazonaws.com:5432/produtos")
    
    produto_repository = ProdutoRepository(session_manager)
    produto_service = ProdutoService(produto_repository)
    ContainerDI.register(ProdutoService, produto_service)
    ContainerDI.register(ProdutoRepository, produto_service)
    
    categoria_repository = CategoriaRepository(session_manager)
    categoria_service = CategoriaService(categoria_repository)
    ContainerDI.register(CategoriaService, categoria_service)
    ContainerDI.register(CategoriaRepository, categoria_service)
    
def register_routers(app):
    # register routes
    blueprint = Blueprint('api', __name__)

    api = Api(blueprint,
          title='Lanchonete da rua - MicroServiço Produtos',
          version='1.0',
          description='Api Restful da lanchonete da rua para microservicos de produtos')

    api.add_namespace(categorias_ns, path='/categorias')
    api.add_namespace(produtos_ns, path='/produtos')
    
    app.register_blueprint(blueprint)

def create_app():
    load_dotenv()
    app = Flask(__name__)
    configure_inject()
    register_routers(app)
    return app

app = create_app()

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')