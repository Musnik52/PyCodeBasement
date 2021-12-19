from sqlalchemy.sql.sqltypes import BigInteger
from flights_db import Base
from sqlalchemy import Column

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger(), nullable=False)
    customer_id = Column(BigInteger(), nullable=False)

    def __repr__(self):
        return f'\n<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'

    def __str__(self):
        return f'<Ticket id={self.id} Flight id={self.flight_id} Customer id={self.customer_id}>'