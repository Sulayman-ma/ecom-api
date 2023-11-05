from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi import crud, schemas, models
from ecomapi.api import deps


router = APIRouter(
    prefix='/cart',
    tags=['cart'],
    responses={
        
    }
)


@router.get("/{id}", response_model=schemas.CartItem)
async def get_cart_item(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get cart item by ID.
    """
    cart_item = await crud.cartitem.get(db=db, id=id)
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'Not Found': "The item went out to get the milk"})
    if not cart_item.id == current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden from accessing this cart item.")
    return cart_item


@router.get("/", response_model=List[schemas.CartItem])
async def get_cart(
    db: AsyncSession = Depends(deps.get_db),
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve all cart items.
    """
    user_id: int = current_user.id
    cart_items = await crud.cartitem.get_multi_by_user(db, user_id=user_id, limit=limit)
    return cart_items


@router.post("/", response_model=schemas.CartItem, status_code=203)
async def add_to_cart(
    *,
    db: AsyncSession = Depends(deps.get_db),
    cart_item_in: schemas.CartItemCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Add item to cart
    Body:
    {
        'quantity': quantity,
        'owner_id': owner_id,
        'product_id': product_id
    }
    """
    cart_item = await crud.cartitem.create(db=db, obj_in=cart_item_in)
    return cart_item


@router.put("/{id}", response_model=schemas.CartItem)
async def update_cart_item(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    cart_item_in: schemas.CartItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a cart item.
    """
    db_cart_item = await crud.cartitem.get(db=db, id=id)
    if not db_cart_item:
        raise HTTPException(status_code=404, detail="item not found")
    cart_item = await crud.cartitem.update(db=db, db_obj=db_cart_item, obj_in=cart_item_in)
    return cart_item


@router.delete("/{id}", response_model=schemas.Product)
async def remove_cart_item(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Remove an item from cart.
    """
    db_cart_item = await crud.cartitem.get(db=db, id=id)
    if not db_cart_item:
        raise HTTPException(status_code=404, detail="cart item not found")
    cart_item = await crud.cartitem.remove(db=db, id=id)
    return cart_item
