from typing import List, Set, Union
from datetime import datetime
from pydantic import BaseModel


class ReadClientRequest(BaseModel):
    limit: Union[int, None] = 100
    
    
class CreateCreditRequest(BaseModel):
    id: Union[int, None] = None 
    credit_card_type: Union[str, None] = None
    credit_card_number: Union[str, None] = None
    currency_code: Union[str, None] = None
    currency: Union[str, None] = None
    useflag: Union[str, None] = 'N'
    
    
class ReadCreditRequest(BaseModel):
    limit: Union[int, None] = 100
    

class UpdateCreditByIdRequest(BaseModel):
    id: Union[int, None] = None
    params: dict
    
    
class DeleteCreditByIdRequest(BaseModel):
    id: Union[int, None] = None 