import jwt
import pendulum

from common import env, exception


class TokenHelper:
    @staticmethod
    def encode(payload: dict, expire_period: int = 30) -> str:
        token = jwt.encode(
            payload={
                **payload,
                "exp": pendulum.now('Asia/Seoul').add(minutes=expire_period),
            },
            key=env.JWT_SECRET_KEY,
            algorithm=env.JWT_ALGORITHM,
        )
        return token

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return jwt.decode(
                token,
                env.JWT_SECRET_KEY,
                env.JWT_ALGORITHM,
            )
        except jwt.exceptions.DecodeError:
            raise exception.DecodeTokenException
        except jwt.exceptions.ExpiredSignatureError:
            raise exception.ExpiredTokenException

    @staticmethod
    def decode_expired_token(token: str) -> dict:
        try:
            return jwt.decode(
                token,
                env.JWT_SECRET_KEY,
                env.JWT_ALGORITHM,
                options={"verify_exp": False},
            )
        except jwt.exceptions.DecodeError:
            raise exception.DecodeTokenException
