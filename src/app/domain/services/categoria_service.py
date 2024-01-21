from app.domain.ports.categoria_repository_port import CategoriaRepositoryPort

class CategoriaService:

    def __init__(self, categoria_repository: CategoriaRepositoryPort) -> None:
        self.categoria_repository  = categoria_repository
 
    def obter_categorias(self):
        return self.categoria_repository.get_all()
        
    def criar_categoria(self, categoria_data):
        return self.categoria_repository.add(categoria_data)

    def obter_categoria_por_id(self, categoria_id):
        return self.categoria_repository.get_by_id(categoria_id)

    def atualizar_categoria(self, categoria_id, categoria_data):
        self.categoria_repository.update(categoria_id, categoria_data)

    def deletar_categoria(self, categoria_id):
        self.categoria_repository.delete(categoria_id)