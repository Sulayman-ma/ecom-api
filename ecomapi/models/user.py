from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, CHAR, DateTime
from sqlalchemy.orm import relationship

from ecomapi.database.database import Base

# if TYPE_CHECKING:
#     from .product import Product  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    gender = Column(CHAR)
    phone = Column(String())
    address = Column(String())
    joined_date = Column(DateTime, default=datetime.now())

    # Relationships
    cartitems = relationship("CartItem", back_populates="user")
