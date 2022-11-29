from db.session import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    regdate =  Column(DateTime(timezone=True), server_default=func.now(), nullable=True)