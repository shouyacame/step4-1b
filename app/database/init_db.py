from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.models import Base
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    # データベース接続URL
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://posuser:{os.getenv('DB_PASSWORD')}@localhost:3306/pos_app"

    # エンジンの作成
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    # テーブルの作成
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!") 