from flask_restx import Namespace, fields

class PingInput:
    api = Namespace('ping', description='apenas um ping')
    ping = api.model('ping', {
        'nome': fields.String(required=True, description='nome do ping')
    })
    
    def __init__(self, nome):
        self.nome = nome
        