import sys
import uvicorn
import pendulum

from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from loguru import logger
from common import env, exception
from config import logger as cnf_logger
from router import index, test, auth
from cache import Cache, KeyMaker, RedisBackend
from middleware import authentication, sqlalchemy


# =============================================================================== #
# ==================================| setting |================================== #
# =============================================================================== #

def init_logger():
    
    def set_datetime(recode):
        recode["extra"]["datetime"] = pendulum.now('Asia/Seoul')
    
    if env.ENV == "dev":
        config = cnf_logger.DevelopConfig()
    elif env.ENV == "production":
        config = cnf_logger.ProductionConfig()
        
    logger.configure(
        handlers=config.LOGURU_SETTINGS['handler'],
        levels=config.LOGURU_SETTINGS['levels']
    )


def init_listener(_app: FastAPI) -> None:
    @_app.exception_handler(exception.BaseException)
    async def exception_handler(request: Request, exc: exception.BaseException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def init_router(_app: FastAPI) -> None:
    _app.include_router(index.index_router, tags=["index"])
    _app.include_router(test.test_router, prefix="/test", tags=["test"])
    _app.include_router(auth.auth_router, prefix="/auth", tags=["auth"])
    
    
def init_cache() -> None:
    Cache.init(backend=RedisBackend(), key_maker=KeyMaker())
    
    
def make_middleware() -> List[Middleware]:

    def on_auth_error(request: Request, exc: Exception):
        status_code, error_code, message = 401, None, str(exc)

        if isinstance(exc, exception.BaseException):
            status_code = int(exc.code)
            error_code = exc.error_code
            message = exc.message

        return JSONResponse(
            status_code=status_code,
            content={"error_code": error_code, "message": message},
        )

    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=[f"http://localhost:{env.API_PORT}"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            authentication.AuthenticationMiddleware,
            backend=authentication.AuthBackend(),
            on_error=on_auth_error,
        ),
        Middleware(sqlalchemy.SQLAlchemyMiddleware),
    ]
    
    return middleware


def create_app() -> FastAPI:
    _app = FastAPI(
        title="fastapi_basic",
        description="fastapi_basic",
        version="1.0.0",
        middleware=make_middleware(),
    )
    
    init_logger()
    init_listener(_app=_app)
    init_router(_app=_app)
    init_cache()

    return _app


# =============================================================================== #
# ===================================| start |=================================== #
# =============================================================================== #

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=env.API_PORT, reload=True)
