from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    email = Column(String, primary_key=True)
    password_hash = Column(String)
    company_name = Column(String)
    encrypted_api_keys = Column(JSON)

# In production, use proper database URL from environment variables
engine = create_engine('sqlite:///./test.db')
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()