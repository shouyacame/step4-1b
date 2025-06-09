from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class ProductBase(BaseModel):
    code: str
    name: str
    price: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class PurchaseItem(BaseModel):
    prd_id: int

class PurchaseRequest(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    items: List[PurchaseItem]

class PurchaseResponse(BaseModel):
    ok: bool
    total: int
