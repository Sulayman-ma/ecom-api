from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi.crud.base import CRUDBase
from ecomapi.models import CartItem
from ecomapi.schemas.cartitem import CartItemCreate, CartItemUpdate


class CRUDItem(CRUDBase[CartItem, CartItemCreate, CartItemUpdate]):
    """"Create a cart item, includes user and product links"""
    async def create(
        self, db: AsyncSession, *, obj_in: CartItemCreate
    ) -> CartItem:
        """"Add a new item to a user's cart"""
        
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi_by_user(
        self, db: AsyncSession, *, user_id: int, limit: int = 100
    ) -> List[CartItem]:
        """"Get all cart items of a single user by ID"""
        
        return (
            await
            db.scalars(select(self.model)
            .filter(CartItem.user_id == user_id)
            .limit(limit)
            )
        )


cartitem = CRUDItem(CartItem)
