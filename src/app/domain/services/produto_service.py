from app.domain.ports.product_repository_port import ProdutoRepositoryPort

class ProdutoService:

    def __init__(self, produto_repository: ProdutoRepositoryPort) -> None:
        self.produto_repository  = produto_repository
 
    def obter_produtos(self):
        return self.produto_repository.get_all()
        
    def criar_produto(self, produto_data):
        return self.produto_repository.add(produto_data)

    def obter_produto_por_id(self, produto_id):
        return self.produto_repository.get_by_id(produto_id)
    
    def obter_produtos_por_categoria_id(self, categoria_id):
        produtos = self.produto_repository.get_all_by_categoria_id(categoria_id)
        
        if produtos is None:
            return None
        
        return produtos
        
    
    def atualizar_produto(self, produto_id, produto_data):
        self.produto_repository.update(produto_id, produto_data)

    def deletar_produto(self, produto_id):
        self.produto_repository.delete(produto_id)