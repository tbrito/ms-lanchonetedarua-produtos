
from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class ProdutoOutput(ma.Schema):
    id = fields.Integer()
    nome = fields.String()
    descricao = fields.String()
    categoria_id = fields.Integer()