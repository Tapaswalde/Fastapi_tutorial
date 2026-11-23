from pydantic import BaseModel,validate_call,ValidationError,StringConstraints,Field
from typing import Annotated


class Item(BaseModel):
    name: str = Field(...,min_length=4)
    description: str | None = None
    price: float


# Data validation without BaseModel
# @validate_call
# def validate(name:Annotated[str,StringConstraints(min_length=4)]):
#     return name


# try:
#     name=validate(name="Aadil")
#     print("name is valid")
# except ValidationError as error:
#     print(f"name is invalid {error}")

try:
    product=Item(name="Calci",price=100)
    product_without_price=product.model_dump(exclude={'price'})
    print(type(product_without_price))
    print(product_without_price)
    print("Product is Valid")
except ValidationError as error:
    print(f"name is invalid {error}")



