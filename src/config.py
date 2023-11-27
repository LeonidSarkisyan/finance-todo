from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = False

DB_HOST = os.environ.get("DB_HOST_TEST") if DEBUG else os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT_TEST") if DEBUG else os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME_TEST") if DEBUG else os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER_TEST") if DEBUG else os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS_TEST") if DEBUG else os.environ.get("DB_PASS")

print(DB_HOST)
print(DB_PORT)
print(DB_NAME)
print(DB_USER)
print(DB_PASS)


class AuthConfig:
    ACCESS_TOKEN_EXPIRE_MINUTES = 3600
    SECRET_KEY = os.environ.get('SECRET_AUTH')
    ALGORITHM = "HS256"
