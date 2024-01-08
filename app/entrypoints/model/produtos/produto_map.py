from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from app.domain.entities.produto import Produto

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ProdutoMap:
    id: int
    nome: str
    descricao: str
    categoria_id: int

    def __init__(self, produto: Produto):
        self.id = produto.id
        self.nome = produto.nome
        self.descricao = produto.descricao
        self.categoria_id = produto.categoria_id

    @classmethod
    def from_entity_list(cls, produtos):
        return [cls(produto) for produto in produtos]