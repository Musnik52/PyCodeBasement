from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import REAL
from db_config import Base

# create a table based on this class
class Company(Base):
    __tablename__ = 'company'

    # static fields
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, nullable=False, default=0)
    address = Column(String(50), nullable=False)
    salary = Column(REAL())

    def __repr__(self):
        return f'\n<User id={self.id} username={self.name} age={self.age} address={self.address}>'

    def __str__(self):
        return f'<User id={self.id} name={self.name} age={self.age} address={self.address}>'