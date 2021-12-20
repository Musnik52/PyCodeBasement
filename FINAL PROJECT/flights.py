from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger
from flights_db import Base
from sqlalchemy import Column, Integer, DateTime

class Flights(Base):
    __tablename__ = 'flights'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    airline_company_id = Column(BigInteger(), ForeignKey('airline_companies.id'), nullable=False)
    origin_country_id = Column(Integer(), nullable=False)
    desitnation_country_id = Column(Integer(), nullable=False)
    departure_time = Column(DateTime(), nullable=False)
    landing_time = Column(DateTime(), nullable=False)
    remaining_tickets= Column(Integer())

    def __repr__(self):
        return f'\n<Flight id={self.id} Airline Co. id={self.airline_company_id} Origin country id={self.origin_country_id} Desitnation country id={self.desitnation_country_id} Departure time={self.departure_time} Landing time={self.landing_time} Remaining tickets={self.remaining_tickets}>'

    def __str__(self):
        return f'<Flight id={self.id} Airline Co. id={self.airline_company_id} Origin country id={self.origin_country_id} Desitnation country id={self.desitnation_country_id} Departure time={self.departure_time} Landing time={self.landing_time} Remaining tickets={self.remaining_tickets}>'
