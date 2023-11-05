# Import all the models, so that Base has them before being
# imported by Alembic
from ecomapi.database.database import Base # noqa
from ecomapi.models.product import Product # noqa
from ecomapi.models.user import User # noqa
from ecomapi.models.cartitem import CartItem # noqa
