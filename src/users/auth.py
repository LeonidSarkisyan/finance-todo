import jwt
from datetime import datetime, timedelta

from src.config import AuthConfig


def create_jwt_token(data: dict, expiration_minutes: int = AuthConfig.ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire_time = datetime.utcnow() + timedelta(minutes=expiration_minutes)
    token_data = {"exp": expire_time, "iat": datetime.utcnow(), **data}
    jwt_token = jwt.encode(token_data, AuthConfig.SECRET_KEY, algorithm=AuthConfig.ALGORITHM)
    return jwt_token


def decode_jwt_token(jtw_token: str) -> dict:
    try:
        decoded_token = jwt.decode(jtw_token, AuthConfig.SECRET_KEY, algorithms=[AuthConfig.ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
