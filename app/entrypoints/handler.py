
from flask import app
from app.adapters import postgresql_query_service
from app.domain.commands import create_product_command, update_product_command
from app.domain.commands_handlers import create_product_command_handler, update_product_command_handler
from app.domain.exceptions.domain_exception import DomainException
from app.domain.middleware import utils
from app.domain.ports import unit_of_work
from app.entrypoints.api.model import api_model

products_query_service = postgresql_query_service.PostgresProductsQueryService(
    "produtos", dynamodb_client.meta.client
)

@app.get("/products/<id>")
def get_product(id: str) -> api_model.GetProductResponse:
    """Returns a single product."""

    product = products_query_service.get_product_by_id(product_id=id)

    if not product:
        raise DomainException(f"Could not locate product with id: {id}.")

    response = api_model.GetProductResponse.parse_obj(product)
    return response.dict()

@app.get("/products")
def list_products() -> api_model.ListProductsResponse:
    """Returns a list of products with paging support."""

    page_size_str = app.current_event.get_query_string_value("pageSize")
    next_token = app.current_event.get_query_string_value("nextToken")

    if not page_size_str or not page_size_str.isnumeric():
        raise DomainException(
            "pageSize should be provided in query string as a number."
        )

    products, last_evaluated_key = products_query_service.list_products(
        page_size=int(page_size_str),
        next_token=next_token,
    )
    products_parsed = [api_model.Product.parse_obj(p.dict()) for p in products]
    response = api_model.ListProductsResponse(
        products=products_parsed, nextToken=last_evaluated_key
    )
    return response.dict()

@app.post("/products")
@utils.parse_event(model=api_model.CreateProductRequest, app_context=app)
def create_product(
    request: api_model.CreateProductRequest,
) -> api_model.CreateProductResponse:
    """Creates a product."""

    id = create_product_command_handler.handle_create_product_command(
        command=create_product_command.CreateProductCommand(
            name=request.name,
            description=request.description,
        ),
        unit_of_work=unit_of_work,
    )
    response = api_model.CreateProductResponse(id=id)
    return response.dict()


@app.put("/products/<id>")
@utils.parse_event(model=api_model.UpdateProductRequest, app_context=app)
def update_product(
    request: api_model.UpdateProductRequest, id: str
) -> api_model.UpdateProductResponse:
    """Updates a product."""

    updated_product_id = update_product_command_handler.handle_update_product_command(
        command=update_product_command.UpdateProductCommand(
            id=id,
            name=request.name,
            description=request.description,
        ),
        unit_of_work=unit_of_work,
    )
    response = api_model.UpdateProductResponse(id=updated_product_id)
    return response.dict()
