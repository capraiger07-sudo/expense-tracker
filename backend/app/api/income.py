from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.income import Income
from app.core.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/income")
def add_income(amount: float, source: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    income = Income(amount=amount, source=source, user_id=1)
    db.add(income)
    db.commit()
    return {"message": "Income added successfully"}

@router.get("/income")
def get_income(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    income = db.query(Income).all()
    return income

@router.put("/income/{id}")
def update_income(id: int, amount: float, source: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    income = db.query(Income).filter(Income.id == id).first()
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    income.amount = amount
    income.source = source
    db.commit()
    return {"message": "Income updated successfully"}

@router.delete("/income/{id}")
def delete_income(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    income = db.query(Income).filter(Income.id == id).first()
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    db.delete(income)
    db.commit()
    return {"message": "Income deleted successfully"}