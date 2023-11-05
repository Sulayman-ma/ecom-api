import secrets
from os import getenv

from dotenv import load_dotenv

from pydantic import EmailStr
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    PROJECT_NAME: str = 'Ecom API'

    # MY_SQL_SERVER: str
    # MY_SQL_USER: str
    # MY_SQL_PASSWORD: str
    # MY_SQL_DB: str
    # Database URL a MySQLDsn for production or an SQLite path for testing
    SQLALCHEMY_DATABASE_URI: str = str(getenv('DB_URL'))

    # Superuser config
    FIRST_SUPERUSER: EmailStr = '25ducks@duck.com'
    FIRST_SUPERUSER_PASSWORD: str = 'faulty'

    PAY_STACK_KEY: str = getenv('PAY_STACK_KEY')

    class Config:
        case_sensitive = True


settings = Settings()
