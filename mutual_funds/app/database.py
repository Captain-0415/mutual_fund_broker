from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

print(f"DATABASE_URL: {DB_URL}")  # Debugging line

engine = create_engine(DB_URL)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

