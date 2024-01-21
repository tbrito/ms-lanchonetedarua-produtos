from app.domain.entities.entity import Entity

class Produto(Entity):
    nome: str
    descricao: str
    categoria_id: int
    def __init__(self, id, nome, descricao, categoria_id, created_at):
        super().__init__(id, created_at)
        self.nome = nome
        self.descricao = descricao
        self.categoria_id = categoria_id