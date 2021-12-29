from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import REAL, BigInteger, Text
from db_config import Base
from sqlalchemy import Column, Integer

class Kita(Base):
    __tablename__ = 'kita'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    floor = Column(Integer())
    num_of_students = Column(Integer())
    class_avg = Column(REAL())

    def __repr__(self):
        return f'\n<Class id={self.id} Floor={self.floor} Number of students={self.num_of_students} Class average={self.class_avg}>'

    def __str__(self):
        return f'<Class id={self.id} Floor={self.floor} Number of students={self.num_of_students} Class average={self.class_avg}>'