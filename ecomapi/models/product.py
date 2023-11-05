from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ecomapi.database.database import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    category = Column(String(), index=True)
    price = Column(Integer, default=0)
    image_url = Column(String())
    added = Column(DateTime, default=datetime.now())

    # Relationships
    cartitems = relationship("CartItem", back_populates="product")
