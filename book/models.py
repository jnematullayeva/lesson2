from sqlalchemy import Integer, String, Column
from database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    desc = Column(String)
    