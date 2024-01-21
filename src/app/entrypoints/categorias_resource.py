from flask_restx import Resource
from flask import jsonify
from app.domain.middleware.response_handler import ResponseHandler
from app.domain.services.categoria_service import CategoriaService
from app.entrypoints.model.categorias.categoria_input import CategoriaInput
from app.entrypoints.model.categorias.categoria_map import CategoriaMap
from container_di import ContainerDI

api = CategoriaInput.api
_categoria = CategoriaInput.categoria

@api.route('/<int:categoria_id>')
class Categorias(Resource):
    @api.doc('obter um categoria por id')
    def get(self, categoria_id):
         categoria_service = ContainerDI.get(CategoriaService)
         categoria = categoria_service.obter_categoria_por_id(categoria_id)
         
         if categoria is None:
             return ResponseHandler.error('Categoria não encontrada', 404)
         
         categoria_dto = CategoriaMap(categoria=categoria)
         return ResponseHandler.success(categoria_dto)

    @api.doc('atualiza um categoria por id')
    @api.expect(_categoria, validate=True)
    def put(self, categoria_id):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_data = api.payload
        categoria = CategoriaInput(**categoria_data)
        
        if categoria_service.obter_categoria_por_id(categoria_id) is None:
            return ResponseHandler.error('Categoria não encontrada')
        
        categoria_service.atualizar_categoria(categoria_id, categoria)
        
        return ResponseHandler.success(status_code=204)

    @api.doc('excluir um categoria por id')
    def delete(self, categoria_id):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_service.deletar_categoria(categoria_id)
        return ResponseHandler.success('Categoria deletado com sucesso')

@api.route('/')
class CategoriasNoParameters(Resource):
    
    def get(self):
        categoria_service = ContainerDI.get(CategoriaService)
        categorias = categoria_service.obter_categorias()
        categorias_dto = CategoriaMap.from_entity_list(categorias)
        return ResponseHandler.success(categorias_dto)

    @api.expect(_categoria, validate=True)
    def post(self):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_data = api.payload
        categoria = CategoriaInput(**categoria_data)
        categoria = categoria_service.criar_categoria(categoria)
        categoria_dto = CategoriaMap(categoria)
        return ResponseHandler.success(data=categoria_dto, status_code=201)