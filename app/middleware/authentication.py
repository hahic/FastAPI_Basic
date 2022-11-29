import jwt
import pendulum

from common import env, exception
from cache import Cache

from datetime import datetime

from typing import Optional, Tuple, Union
from pydantic import BaseModel
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware as BaseAuthenticationMiddleware
from starlette.requests import HTTPConnection


class CurrentUser(BaseModel):
    role: Union[None, str] = None
    exp: Union[None, datetime] = None

    class Config:
        validate_assignment = True


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            scheme, credentials = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
            if not credentials:
                return False, current_user
        except ValueError:
            return False, current_user
        
        try:
            payload = jwt.decode(
                credentials,
                env.JWT_SECRET_KEY,
                algorithms=[env.JWT_ALGORITHM],
            )
            role = payload.get("role")
            exp = payload.get("exp")
            
        except jwt.exceptions.PyJWTError:
            return False, current_user

        current_user.role = role
        current_user.exp = pendulum.from_timestamp(exp, tz="Asia/Seoul")
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass