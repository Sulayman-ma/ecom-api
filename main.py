from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ecomapi.api.routers import auth, users, products, admin, carts
from ecomapi.core.config import settings

# Main app instance
app = FastAPI(
    title=settings.PROJECT_NAME,
)

# Including application routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(admin.router)
app.include_router(carts.router)
app.include_router(auth.router)

# Adding middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Index Page Route
@app.get('/')
async def root():
    return {'Hello': 'This is my Fast API app with home page(root)'}
