from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from app.domain.entities.categoria import Categoria

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CategoriaMap:
    id: int
    nome: str

    def __init__(self, categoria: Categoria):
        self.id = categoria.id
        self.nome = categoria.nome

    @classmethod
    def from_entity_list(cls, categorias):
        return [cls(categoria) for categoria in categorias]