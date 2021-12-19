from sqlalchemy.sql.sqltypes import BigInteger, Integer, Text
from flights_db import Base
from sqlalchemy import Column

class Administrators(Base):
    __tablename__ = 'administrators'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(Text(), nullable=False, unique=True)
    last_name = Column(Text(), nullable=False, unique=True)
    user_id = Column(BigInteger(), unique=True)

    def __repr__(self):
        return f'\n<Administrator id={self.id} First name={self.first_name} Last name={self.last_name} User id={self.user_id}>'

    def __str__(self):
        return f'<Administrator id={self.id} First name={self.first_name} Last name={self.last_name} User id={self.user_id}>'