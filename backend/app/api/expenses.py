from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.core.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/expenses")
def add_expense(amount: float, category: str, note: str = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    expense = Expense(amount=amount, category=category, note=note, user_id=1)
    db.add(expense)
    db.commit()
    return {"message": "Expense added successfully"}

@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    expenses = db.query(Expense).all()
    return expenses

@router.put("/expenses/{id}")
def update_expense(id: int, amount: float, category: str, note: str = None, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    expense = db.query(Expense).filter(Expense.id == id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense.amount = amount
    expense.category = category
    expense.note = note
    db.commit()
    return {"message": "Expense updated successfully"}

@router.delete("/expenses/{id}")
def delete_expense(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    expense = db.query(Expense).filter(Expense.id == id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}