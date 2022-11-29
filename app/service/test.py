from typing import Optional, List
from sqlalchemy import select, update, delete, or_, and_

from db import Transactional, Propagation, session
from db.schema import Client, CreditCard
from common import exception


class TestService:
    async def read_client(self, limit: int) -> List[Client]:
        query = select(Client)
        query = query.limit(limit)
        result = await session.execute(query)
        
        return result.scalars().all()
    
    
    @Transactional(propagation=Propagation.REQUIRED)
    async def create_credit(
        self, 
        id: int, 
        credit_card_type: str, 
        credit_card_number: str, 
        currency_code: str, 
        currency: str, 
        useflag: str
    ) -> dict[str, str]:
        if id is None:
            raise exception.BadRequestException
        
        query = select(CreditCard).where(CreditCard.id == id)
        result = await session.execute(query)
        
        is_exist = result.scalars().first()
        if is_exist:
            raise exception.DuplicateValueException

        credit = CreditCard(
            id=id, 
            credit_card_type=credit_card_type, 
            credit_card_number=credit_card_number, 
            currency_code=currency_code, 
            currency=currency, 
            useflag=useflag
        )
        session.add(credit)
        
        return {'id': id}
    
    
    async def read_credit(self, limit: int) -> List[CreditCard]:
        query = select(CreditCard)
        query = query.limit(limit)
        result = await session.execute(query)
        
        return result.scalars().all()
    
    
    @Transactional(propagation=Propagation.REQUIRED)
    async def update_credit_by_id(self, id: int, params: dict) -> dict[str, str]:
        if id is None:
            raise exception.BadRequestException
        
        query = select(CreditCard).where(CreditCard.id == id)
        result = await session.execute(query)
        
        is_exist = result.scalars().first()
        if is_exist is None:
            raise exception.NotExistValueException
        
        query = (
            update(CreditCard)
            .where(CreditCard.id == id)
            .values(params)
        )
        await session.execute(query)
        
        return {'id': id}
    
    
    @Transactional(propagation=Propagation.REQUIRED)
    async def delete_credit_by_id(self, id: int) -> dict:
        if id is None:
            raise exception.BadRequestException
        
        query = select(CreditCard).where(CreditCard.id == id)
        result = await session.execute(query)
        
        data = result.scalars().first()
        if data is None:
            raise exception.NotExistValueException
        
        query = (
            delete(CreditCard)
            .where(CreditCard.id == id)
        )
        await session.execute(query)
        
        return data
        