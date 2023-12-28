import typing
from abc import ABC, abstractmethod

from app.domain.model import product
from app.domain.ports.product_repository import ProductsRepository

class UnitOfWork(ABC):
    products: ProductsRepository
 
    @abstractmethod
    def commit(self) -> None:
        ...

    @abstractmethod
    def __enter__(self) -> typing.Any:
        ...

    @abstractmethod
    def __exit__(self, *args) -> None:
        ...