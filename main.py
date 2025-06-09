from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import models
from app.schemas import schemas
from decimal import Decimal
from typing import Optional

app = FastAPI(title="POS System API")

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to POS System API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/product/{code}")
def get_product(code: str, db: Session = Depends(get_db)):
    product = db.query(models.ProductMaster).filter(models.ProductMaster.code == code).first()
    if product is None:
        return None
    return {
        "id": product.id,
        "code": product.code,
        "name": product.name,
        "price": int(product.price),
    }

@app.post("/purchase")
def create_purchase(purchase: dict, db: Session = Depends(get_db)):
    emp_cd = purchase.get("emp_cd") or "9999999999"
    store_cd = purchase.get("store_cd") or "30"
    pos_no = purchase.get("pos_no") or "90"
    items = purchase.get("items", [])

    # 取引登録
    transaction = models.Transaction(
        emp_cd=emp_cd,
        store_cd=store_cd,
        pos_no=pos_no,
        total_amt=0
    )
    db.add(transaction)
    db.flush()  # IDを取得

    total = 0
    for i, item in enumerate(items, 1):
        prd_id = item.get("prd_id")
        product = db.query(models.ProductMaster).filter(models.ProductMaster.id == prd_id).first()
        if not product:
            db.rollback()
            return {"ok": False, "total": 0}
        detail = models.TransactionDetail(
            trd_id=transaction.id,
            dtl_id=i,
            prd_id=product.id,
            prd_code=product.code,
            prd_name=product.name,
            prd_price=int(product.price)
        )
        db.add(detail)
        total += int(product.price)

    # 合計金額を更新
    transaction.total_amt = total
    db.commit()

    return {"ok": True, "total": total}

import uvicorn

app = FastAPI(title="POS System API")

# CORSやルーティング定義は省略（そのままでOK）

# このブロックの末尾に以下を追加してください
uvicorn.run(app, host="0.0.0.0", port=8000)
