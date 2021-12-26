from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text
from flights_db import Base
from sqlalchemy import Column, Integer

class AirlineCompanies(Base):
    __tablename__ = 'airline_companies'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False, unique=True)
    country_id = Column(BigInteger(), ForeignKey('countries.id'), unique=False, nullable=False)
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)

    def __repr__(self):
        return f'\n<Airline Co. id={self.id} Name={self.name} Country id={self.country_id} User id={self.user_id}>'

    def __str__(self):
        return f'<Airline Co. id={self.id} Name={self.name} Country id={self.country_id} User id={self.user_id}>'
