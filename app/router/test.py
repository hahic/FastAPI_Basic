from model import test as md_test
from typing import Union, List, Dict
from fastapi import APIRouter, HTTPException, status

from controller import test as ct_test
from loguru import logger
from common import exception

test_router = APIRouter()


@test_router.get('/data', response_model=Dict[str, List[md_test.Test]])
async def read_test():
    try:
        data = await ct_test.read_bigquery_data()
        data = data.to_dict(orient = 'records')

        return {'data': data}

    except Exception as ex:
        logger.error(ex)


@test_router.get('/exception/{id}', response_model=Dict[str, List[md_test.Test]])
async def exception_test(id: int):
    data = await ct_test.read_bigquery_data()
    data = data.to_dict(orient = 'records')

    if id == 2:
        raise exception.BadRequestException('test1')

    return {'data': data}
