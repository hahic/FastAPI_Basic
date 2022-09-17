from fastapi import APIRouter
from typing import Union, List, Dict

index_router = APIRouter()


@index_router.get('/', response_model=Dict[str, str])
def home():
    return {
        'writer': '임어진', 
        'create_date': '2022-09-01'
        }
