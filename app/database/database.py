from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Azure MySQL接続情報
SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://tech0sql1:step4pos-1@rdbs-step4-north-europe.mysql.database.azure.com:3306/rdbs-step4-north-europe"
    "?ssl_mode=REQUIRED"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
