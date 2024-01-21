
from app.domain.entities.entity import Entity

class Categoria(Entity):
    nome: str
    
    def __init__(self, id, nome, created_at):
        super().__init__(id, created_at)
        self.nome = nome