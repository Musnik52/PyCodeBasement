from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

connection_string = 'postgresql+psycopg2://postgres:admin@localhost/tourism'
Base = declarative_base()
engine = create_engine(connection_string, echo=True)

def create_all_entities():
    Base.metadata.create_all(engine)

Session = sessionmaker()
local_session = Session(bind=engine)