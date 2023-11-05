import logging
import asyncio

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ecomapi.api import deps
from ecomapi.database.init_db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init() -> None:
    db = deps.get_db()
    await init_db(db)


async def main() -> None:
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())
