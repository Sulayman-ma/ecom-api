from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None


# Properties to receive on product creation
class ProductCreate(ProductBase):
    title: str
    price: int


# Properties to receive on product update
class ProductUpdate(ProductBase):
    category: str | None = None
    image_url: str | None = None


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    title: str
    price: int

    class Config:
        from_attributes = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Additional properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
