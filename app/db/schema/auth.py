from db.session import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func


class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=True)
    useflag = Column(String, nullable=True)
    regdate =  Column(DateTime(timezone=True), server_default=func.now(), nullable=True)