from abc import ABC, abstractmethod

class ProdutoRepositoryPort(ABC):
    @abstractmethod
    def get_by_id(self, produto_id):
        """Obter usuario pelo id."""
        pass

    @abstractmethod
    def get_all(self):
        """Obter todos os usuário."""
        pass
    
    
    @abstractmethod
    def get_all_by_categoria_id(self, categoria_id):
        """Obter todos os usuário."""
        pass

    @abstractmethod
    def add(self, produto):
        """Cadastrar novo usuário."""
        pass

    @abstractmethod
    def update(self, produto_id, produto):
        """Atualizar um usuário."""    
        pass

    @abstractmethod
    def delete(self, produto_id):
        """Excluir um usuário.""" 
        pass   