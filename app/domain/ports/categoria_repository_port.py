from abc import ABC, abstractmethod

class CategoriaRepositoryPort(ABC):
    @abstractmethod
    def get_by_id(self, categoria_id):
        """Obter usuario pelo id."""
        pass

    @abstractmethod
    def get_all(self):
        """Obter todos os categoria."""
        pass

    @abstractmethod
    def add(self, categoria):
        """Cadastrar novo categoria."""
        pass

    @abstractmethod
    def update(self, categoria_id, categoria):
        """Atualizar um categoria."""    
        pass

    @abstractmethod
    def delete(self, categoria_id):
        """Excluir um categoria.""" 
        pass   