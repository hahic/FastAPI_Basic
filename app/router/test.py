from typing import Union, List, Dict
from fastapi import APIRouter, Depends 
from loguru import logger

from common.permission import *
from model.test import request, response
from service.test import TestService 


test_router = APIRouter()


@test_router.post(
    '/read/client', 
    response_model=Dict[str, List[response.ReadClientResponse]], 
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
async def read_client(request: request.ReadClientRequest):
    data = await TestService().read_client(**request.dict())
    data = [dict(x.__dict__.items()) for x in data]
    return {'data': data}


@test_router.post(
    '/create/credit', 
    response_model=Dict[str, response.CreateCreditResponse],
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
async def create_credit(request: request.CreateCreditRequest):
    data = await TestService().create_credit(**request.dict())
    return {'data': data}


@test_router.post(
    '/read/credit', 
    response_model=Dict[str, List[response.ReadCreditResponse]],
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
async def read_credit(request: request.ReadCreditRequest):
    data = await TestService().read_credit(**request.dict())
    data = [dict(x.__dict__.items()) for x in data]
    return {'data': data}
        

@test_router.post(
    '/update/credit/byid', 
    response_model=Dict[str, response.UpdateCreditByIdResponse],
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
async def update_credit_by_id(request: request.UpdateCreditByIdRequest):
    data = await TestService().update_credit_by_id(**request.dict())
    return {'data': data}
        

@test_router.post(
    '/delete/credit/byid', 
    response_model=Dict[str, response.DeleteCreditByIdResponse],
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
async def delete_credit_by_id(request: request.DeleteCreditByIdRequest):
    data = await TestService().delete_credit_by_id(**request.dict())
    data = dict(data.__dict__.items())
    return {'data': data}
        
        
