from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column

class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False)
    price = Column(REAL(), nullable=False)

    def __repr__(self):
        return f'\n<Attraction id={self.id} Name={self.name} Price={self.price}>'

    def __str__(self):
        return f'\n<Attraction id={self.id} Name={self.name} Price={self.price}>'
