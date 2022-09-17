import sys
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from loguru import logger
from common import env, exception
from config import logger as cnf_logger
from router import test, index


# =============================================================================== #
# ==================================| setting |================================== #
# =============================================================================== #

def init_logger():
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


def create_app() -> FastAPI:
    _app = FastAPI()

    init_logger()
    init_listener(_app=_app)
    init_router(_app=_app)

    return _app


# =============================================================================== #
# ===================================| start |=================================== #
# =============================================================================== #

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=env.API_PORT, reload= True)
