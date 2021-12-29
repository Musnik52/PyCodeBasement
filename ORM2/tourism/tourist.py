from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column

class Tourist(Base):
    __tablename__ = 'tourists'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False)
    origin_country = Column(Text(), nullable=False)

    def __repr__(self):
        return f'\n<Tourist id={self.id} Name={self.name} Origin country={self.origin_country}>'

    def __str__(self):
        return f'\n<Tourist id={self.id} Name={self.name} Origin country={self.origin_country}>'
