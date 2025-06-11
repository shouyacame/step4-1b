from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, CHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database.database import Base

class ProductMaster(Base):
    __tablename__ = "product_master"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(CHAR(13), unique=True, index=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, default=datetime.utcnow)
    emp_cd = Column(String(10))
    store_cd = Column(String(10))
    pos_no = Column(String(10))
    total_amt = Column(Numeric(10, 2))
    
    details = relationship("TransactionDetail", back_populates="transaction")

class TransactionDetail(Base):
    __tablename__ = "transaction_detail"

    trd_id = Column(Integer, ForeignKey("transaction.id"), primary_key=True)
    dtl_id = Column(Integer, primary_key=True)
    prd_id = Column(Integer, ForeignKey("product_master.id"))
    prd_code = Column(CHAR(13))
    prd_name = Column(String(100))
    prd_price = Column(Numeric(10, 2))
    qty = Column(Integer)

    transaction = relationship("Transaction", back_populates="details")
