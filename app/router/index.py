from fastapi import APIRouter
from typing import Union, List, Dict

index_router = APIRouter()


@index_router.get('/', response_model=Dict[str, str])
def home():
    return {
        'writer': '임어진', 
        'created date': '2022-09-01',
        'last modifieddate': '2022-11-29'
        }
