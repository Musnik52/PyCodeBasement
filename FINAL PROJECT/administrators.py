from db_config import Base
from sqlalchemy import Column, UniqueConstraint, BigInteger, Text, ForeignKey

class Administrators(Base):
    __tablename__ = 'administrators'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(Text(), nullable=False)
    last_name = Column(Text(), nullable=False)
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)

    __table_args__= (UniqueConstraint('first_name', 'last_name', name='una_1'),)

    def __repr__(self):
        return f'\n<Administrator id={self.id} First name={self.first_name} Last name={self.last_name} User id={self.user_id}>'

    def __str__(self):
        return f'<Administrator id={self.id} First name={self.first_name} Last name={self.last_name} User id={self.user_id}>'