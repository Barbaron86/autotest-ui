from pydantic import BaseModel, Field


class Market(BaseModel):
    name: str
    id: int


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(..., gt=0, description="Price of the product must be greater than 0")
    tags: list[str] = []
    market: Market


product_data = {
    "id": 1,
    "name": "Product 1",
    "price": 100.5,
    "tags": ["electronics", "smartphones"],
    "market": {"name": "Market 1", "id": 1},
}

product = Product(**product_data)  # type: ignore[arg-type]
print(product)

new_product = Product(
    id=2, name="Product 2", price=200.5, tags=["electronics", "smartphones"], market=Market(name="Market 2", id=2)
)
print(new_product)
