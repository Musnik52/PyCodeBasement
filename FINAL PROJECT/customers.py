from sqlalchemy.sql.sqltypes import BigInteger, Text
from flights_db import Base
from sqlalchemy import Column

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(Text(), nullable=False, unique=True)
    last_name = Column(Text(), nullable=False, unique=True)
    address = Column(Text(), nullable=False, unique=True)
    phone_number = Column(Text(), nullable=False, unique=True)
    credit_card_number = Column(Text(), nullable=False, unique=True)
    user_id = Column(BigInteger(), unique=True)

    def __repr__(self):
        return f'\n<Customer id={self.id} First name={self.first_name} Last name={self.last_name} Address={self.address} Phone number={self.phone_number} Credit-card number={self.credit_card_number} User id={self.user_id}>'

    def __str__(self):
        return f'<Customer id={self.id} First name={self.first_name} Last name={self.last_name} Address={self.address} Phone number={self.phone_number} Credit-card number={self.credit_card_number} User id={self.user_id}>'