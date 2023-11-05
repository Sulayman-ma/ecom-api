from pydantic import BaseModel


# Shared properties
class CartItemBase(BaseModel):
    quantity: int | None = None


# Properties to receive on CartItem creation
class CartItemCreate(CartItemBase):
    owner_id: int
    product_id: int


# Properties to receive on CartItem update
class CartItemUpdate(CartItemBase):
    pass


# Properties shared by models stored in DB
class CartItemInDBBase(CartItemBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class CartItem(CartItemInDBBase):
    id: int
    owner_id: int
    product_id: int


# Additional properties stored in DB
class CartItemInDB(CartItemInDBBase):
    pass
