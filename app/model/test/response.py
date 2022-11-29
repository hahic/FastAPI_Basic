from typing import List, Set, Union
from datetime import datetime
from pydantic import BaseModel


class ReadClientResponse(BaseModel):
    id: Union[int, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[str, None] = None
    gender: Union[str, None] = None
    ip_address: Union[str, None] = None
    regdate: Union[datetime, None] = None
    
    
class CreateCreditResponse(BaseModel):
    id: Union[int, None] = None 
    
    
class ReadCreditResponse(BaseModel):
    id: Union[int, None] = None
    credit_card_type: Union[str, None] = None
    credit_card_number: Union[str, None] = None
    currency_code: Union[str, None] = None
    currency: Union[str, None] = None
    useflag: Union[str, None] = None
    regdate: Union[datetime, None] = None
    

class UpdateCreditByIdResponse(BaseModel):
    id: Union[int, None] = None 
    
    
class DeleteCreditByIdResponse(BaseModel):
    id: Union[int, None] = None 
    credit_card_type: Union[str, None] = None
    credit_card_number: Union[str, None] = None
    currency_code: Union[str, None] = None
    currency: Union[str, None] = None
    useflag: Union[str, None] = None
    regdate: Union[datetime, None] = None
    