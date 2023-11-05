from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi import crud, schemas, models
from ecomapi.api import deps

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
    responses={
        418: {'description': 'I am a teapot'},
        203: {'Created': 'Successfully'}
    }
)


@router.post("/products", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    *,
    db: AsyncSession = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create a new product (ADMIN ONLY).
    Sample body:
    {
        'title': 'product title here',
        'price': 0.00,
        [optional]
        'description': 'lorem ipsum gucci diorrrr balenciaga',
        'category': 'Versace',
        'image_url': 'url of image here'
    }
    """
    product = await crud.product.create(db=db, obj_in=product_in)
    return product


@router.put("/products/{id}", response_model=schemas.Product, status_code=status.HTTP_202_ACCEPTED)
async def update_product(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    product_in: schemas.ProductUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a product (ADMIN ONLY).
    """
    product = await crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    product = await crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.delete("/products/{id}", response_model=schemas.Product, status_code=status.HTTP_200_OK)
async def delete_product(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an product (ADMIN ONLY).
    """
    product = await crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    product = await crud.product.remove(db=db, id=id)
    return product


@router.delete("/users/{id}", response_model=schemas.User)
async def delete_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete a user
    """
    user = await crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await crud.user.remove(db=db, id=id)
    return user


@router.get("/users", response_model=List[schemas.User])
async def get_users(
    db: AsyncSession = Depends(deps.get_db),
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all users.
    """
    users = await crud.user.get_multi(db, skip=0, limit=limit)
    return users
