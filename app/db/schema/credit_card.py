from db.session import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func


class CreditCard(Base):
    __tablename__ = "credit_card"

    id = Column(Integer, primary_key=True)
    credit_card_type = Column(String, nullable=True)
    credit_card_number = Column(String, nullable=True)
    currency_code = Column(String, nullable=True)
    currency = Column(String, nullable=True)
    useflag = Column(String, nullable=True)
    regdate = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)