from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ecomapi.database.database import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class CartItem(Base):
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    
    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    user = relationship('User', uselist=False, back_populates='cartitems')
    product = relationship('Product', uselist=False, back_populates='cartitems')
