import typing
from abc import ABC, abstractmethod
from app.domain.model import product

class ProductsRepository(ABC):
    @abstractmethod
    def add(self, product: product.Product) -> None:
        ...

    @abstractmethod
    def update_attributes(self, product_id: str, **kwargs) -> None:
        ...

    @abstractmethod
    def get(self, product_id: str) -> typing.Optional[product.Product]:
        ...

    @abstractmethod
    def delete(self, product_id: str) -> None:
        ...
