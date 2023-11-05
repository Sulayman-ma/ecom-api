from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi.crud.base import CRUDBase
from ecomapi.models import Product
from ecomapi.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    async def get_category(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 50, category: str
    ) -> List[Product]:
        return (
            await
            db.scalars(select(self.model)
            .filter(Product.category == category)
            .offset(skip)
            .limit(limit)
            )
        )


product = CRUDProduct(Product)
