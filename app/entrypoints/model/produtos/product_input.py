from flask_restx import Namespace, fields

class ProdutoInput:
    api = Namespace('produtos', description='operações relacionadas a produtos')
    produto = api.model('produtos', {
        'nome': fields.String(required=True, description='nome do produto'),
        'categoria_id': fields.Integer(required=True, description='Id da Categoria'),
        'descricao': fields.String(required=True, description='descrição do produto')
    })
    
    def __init__(self, nome, categoria_id, descricao):
        self.nome = nome
        self.categoria_id = categoria_id
        self.descricao = descricao