from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False)

    def __repr__(self):
        return f'\n<Teacher id={self.id} Name={self.name}>'

    def __str__(self):
        return f'<Teacher id={self.id} FName={self.name} >'