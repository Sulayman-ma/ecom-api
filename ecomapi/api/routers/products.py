from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi import crud, schemas
from ecomapi.api import deps


router = APIRouter(
    prefix='/products',
    tags=['products'],
    responses={
        
    }
)


@router.get("/", response_model=List[schemas.Product])
async def get_prodcuts(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve all products.
    """
    products = await crud.product.get_multi(db, skip=skip, limit=limit)
    return products


@router.get("/category/{category}", response_model=List[schemas.Product])
async def get_category(
    category: str,
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve list of products in a category.
    """
    products = await crud.product.get_category(db, skip=skip, limit=limit, category=category)
    return products


@router.get("/{id}", response_model=schemas.Product)
async def get_product(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get product by ID.
    """
    product = await crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail={'Not Found': "The product went out to get the milk"})
    # if not await crud.user.is_superuser(current_user):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return product


@router.post("/{id}", response_model=schemas.Product)
async def buy_now(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    price: int,
) -> Any:
    pass
