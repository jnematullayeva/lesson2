from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker




# avval postgresmi kn username va passwordmi yozamiz
DATABASE_URL = 'postgresql://postgres:3698@localhost:5432/fasrapin77'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )
Base = declarative_base()
