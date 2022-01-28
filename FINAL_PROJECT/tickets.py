from db_config import Base
from sqlalchemy import Column, UniqueConstraint, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger(), ForeignKey('flights.id'), nullable=False)
    customer_id = Column(BigInteger(), ForeignKey('customers.id'), nullable=False)

    __table_args__= (UniqueConstraint('flight_id', 'customer_id', name='una_3'),)
    
    flights = relationship('Flights', backref=backref('tickets', uselist=True))
    customers = relationship('Customers', backref=backref('tickets', uselist=True))

    def __repr__(self):
        return f'\n<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'

    def __str__(self):
        return f'<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'