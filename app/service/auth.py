from model.auth.schema import RefreshTokenSchema
from common.exception import DecodeTokenException, ExpiredTokenException
from common.utils import TokenHelper

from sqlalchemy import select, update, and_
from db import Transactional, Propagation, session
from db.schema import Auth

import pendulum


class JwtService:
    async def verify_token(self, token: str) -> None:
        data = TokenHelper.decode(token=token)
        
        exp = pendulum.from_timestamp(data["exp"], tz="Asia/Seoul")
        if exp <= pendulum.now('Asia/Seoul'):
            raise ExpiredTokenException
        
        
    @Transactional(propagation=Propagation.REQUIRED)
    async def create_token(self, role: str) -> str:
        query = select(Auth).where(Auth.role == role)
        data = await session.execute(query)
        
        auth = data.scalars().first()
        if auth:
            return TokenHelper.encode(payload={"role": auth.role})
        
        new_data = Auth(
            role=role, 
            useflag='Y'
        )
        session.add(new_data)
        
        return TokenHelper.encode(payload={"role": new_data.role})


    async def refresh_token(self, token: str, refresh_token: str) -> RefreshTokenSchema:
        token = TokenHelper.decode(token=token)
        refresh_token = TokenHelper.decode(token=refresh_token)
        if refresh_token.get("sub") != "refresh":
            raise DecodeTokenException

        return RefreshTokenSchema(
            token=TokenHelper.encode(payload={"user_id": token.get("user_id")}),
            refresh_token=TokenHelper.encode(payload={"sub": "refresh"}),
        )
