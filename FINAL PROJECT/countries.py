from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import Text
from db_config import Base
from sqlalchemy import Column, BigInteger

class Countries(Base):
    __tablename__ = 'countries'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False, unique=True)

    def __repr__(self):
        return f'\n<Country id={self.id} Name={self.name}>'

    def __str__(self):
        return f'<Country id={self.id} Name={self.name}>'