from ast import List, Tuple
from typing import Any, Optional
from app.adapters.postgres_unit_of_work import DBPrefix, PostgresProductsRepository
from app.domain.model import product
from app.domain.ports import products_query_service


class PostgresProductsQueryService(products_query_service.ProductsQueryService):
    """Products Postgres query service."""

    def __init__(self, table_name: str, postgres_client: client.DynamoDBClient):
        self._table_name = table_name
        self._postgres_client = postgres_client

    def list_products(
        self, page_size: int, next_token: Any
    ) -> Tuple[List[product.Product], Any]:
        """Returns a list of all products in repository with paging after 1 MB."""

        if next_token:
            result = self._postgres_client.scan(
                TableName=self._table_name,
                Limit=page_size,
                FilterExpression=Key("PK").begins_with(f"{DBPrefix.PRODUCT.value}#")
                & Key("SK").begins_with(f"{DBPrefix.PRODUCT.value}#"),
                ExclusiveStartKey=next_token,
            )
        else:
            result = self._postgres_client.scan(
                TableName=self._table_name,
                Limit=page_size,
                FilterExpression=Key("PK").begins_with(f"{DBPrefix.PRODUCT.value}#")
                & Key("SK").begins_with(f"{DBPrefix.PRODUCT.value}#"),
            )

        products = [product.Product.parse_obj(item) for item in result["Items"]]

        if "LastEvaluatedKey" in result:
            return products, result["LastEvaluatedKey"]
        else:
            return products, None

    def get_product_by_id(self, product_id: str) -> Optional[product.Product]:
        """Returns a single product by ID."""

        product_response = self._postgres_client.get_item(
            TableName=self._table_name,
            Key=PostgresProductsRepository.generate_product_key(product_id),
        )

        return (
            product.Product.parse_obj(product_response["Item"])
            if product_response["Item"]
            else None
        )