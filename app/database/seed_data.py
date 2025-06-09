from sqlalchemy.orm import Session
from ..models.models import ProductMaster
from ..database.database import SessionLocal
import os
from dotenv import load_dotenv

load_dotenv()

def seed_data():
    db = SessionLocal()
    try:
        # サンプル商品データ
        products = [
            ProductMaster(code="4901234567890", name="商品A", price=1000),
            ProductMaster(code="4902345678901", name="商品B", price=2000),
            ProductMaster(code="4903456789012", name="商品C", price=3000),
        ]

        # データベースに追加
        for product in products:
            db.add(product)
        
        # 変更をコミット
        db.commit()
        print("Sample data seeded successfully!")
    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data() 