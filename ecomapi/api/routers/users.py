from typing import Any

from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr

from ecomapi import schemas, models, crud
from ecomapi.api import deps


router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={
        404: {'description': 'Not found'}
    }
)


@router.get('/profile', response_model=schemas.User)
async def profile(
    current_user: models.User = Depends(deps.get_current_active_user)
) -> models.User:
    return current_user


@router.post("/signup", response_model=schemas.User)
async def create_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    user = await crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists.",
        )
    user_in = schemas.UserCreate( 
        email=email,
        password=password,
        full_name=full_name,
    )
    user = await crud.user.create(db, obj_in=user_in)
    return user
