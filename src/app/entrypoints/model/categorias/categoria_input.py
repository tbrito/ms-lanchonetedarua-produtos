from flask_restx import Namespace, fields

class CategoriaInput:
    api = Namespace('categorias', description='operações relacionadas a categorias')
    categoria = api.model('categorias', {
        'nome': fields.String(required=True, description='nome do categorias')
    })
    
    def __init__(self, nome):
        self.nome = nome
        