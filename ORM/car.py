from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_config import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    model = Column(String(25), nullable=False, unique=True)
    brand = Column(String(80), nullable=False, unique=True, index=True) 
    year = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f'\n<Car id={self.id} Model ={self.model} Brand ={self.brand} Year ={self.year}>'

    def __str__(self):
        return f'<Car id={self.id} Model ={self.model} Brand ={self.brand} Year ={self.year}>'
