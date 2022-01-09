from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger
from db_config import Base
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.orm import relationship, backref

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger(), ForeignKey('flights.id'), nullable=False)
    customer_id = Column(BigInteger(), ForeignKey('customers.id'), nullable=False)
    
    flights = relationship('Flights', backref=backref('tickets', uselist=True))
    customers = relationship('Customers', backref=backref('tickets', uselist=True))

    def __repr__(self):
        return f'\n<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'

    def __str__(self):
        return f'<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'