from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship, backref

class Student(Base):
    __tablename__ = 'students'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(Text(), nullable=False, unique=True)
    last_name = Column(Text(), nullable=False, unique=True)
    grade_avg = Column(REAL())
    kita_id = Column(BigInteger(), ForeignKey('kita.id'))

    kitot = relationship('Kita', backref=backref('students', uselist=True))

    def __repr__(self):
        return f'\n<Student id={self.id} First name={self.first_name} Last name={self.last_name} Grade average={self.grade_avg} Kita idr={self.kita_id}>'

    def __str__(self):
        return f'<Student id={self.id} First name={self.first_name} Last name={self.last_name} Grade average={self.grade_avg} Kita idr={self.kita_id}>'