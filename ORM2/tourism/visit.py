from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Text, REAL
from db_config import Base
from sqlalchemy import Column
from sqlalchemy.orm import backref, relation, relationship

class Visit(Base):
    __tablename__ = 'visits'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    tourist_id = Column(BigInteger(), ForeignKey('tourists.id'), nullable=False)
    attraction_id = Column(BigInteger(), ForeignKey('attractions.id'), nullable=False)
    year_of_visit = Column(BigInteger(), nullable=False)
    tourists = relationship('Tourist', backref=backref("visits", uselist=True))
    attractions = relationship('Attraction', backref=backref("visits", uselist=True))


    def __repr__(self):
        return f'\n<Visit id={self.id} Tourist id={self.tourist_id} attraction id={self.attraction_id} Year of visit={self.year_of_visit}>'

    def __str__(self):
        return f'\n<Visit id={self.id} Tourist id={self.tourist_id} attraction id={self.attraction_id} Year of visit={self.year_of_visit}>'

