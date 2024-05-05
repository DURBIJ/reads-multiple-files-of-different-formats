from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class FileData(Base):
    __tablename__ = 'file_data'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content = Column(Text)

# create database tables based 
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
