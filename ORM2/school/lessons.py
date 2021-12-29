from sqlalchemy.orm import backref, relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column, Table, Date, UniqueConstraint

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    subject_id = Column(BigInteger(), ForeignKey('subjects.id'), nullable=False)
    teacher_id = Column(BigInteger(), ForeignKey('teachers.id'), nullable=False)
    student_id = Column(BigInteger(), ForeignKey('students.id'), nullable=False)
    student = relationship('Student', backref=backref("lessons", uselist=True))
    teacher = relationship('Teacher', backref=backref("lessons", uselist=True))
    subject = relationship('Subject', backref=backref("lessons", uselist=True))

    def __repr__(self):
        return f'\n<Lesson id={self.id} Student id={self.student_id} Teacher id={self.teacher_id} Subject id={self.subject_id}>'

    def __str__(self):
        return f'<Lesson id={self.id} Student id={self.student_id} Teacher id={self.teacher_id} Subject id={self.subject_id}>'