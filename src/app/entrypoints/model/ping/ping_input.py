from flask_restx import Namespace, fields

class PingInput:
    api = Namespace('testandoping', description='apenas um testandoping')
    ping = api.model('testandoping', {
        'nome': fields.String(required=True, description='nome do testandoping')
    })
    
    def __init__(self, nome):
        self.nome = nome
        