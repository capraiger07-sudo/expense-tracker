from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal
from app.models.expense import Expense
from app.models.income import Income
from app.core.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def get_summary(month: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    
    expenses = db.query(func.sum(Expense.amount)).filter(
        func.to_char(Expense.date, 'YYYY-MM') == month
    ).scalar() or 0

    income = db.query(func.sum(Income.amount)).filter(
        func.to_char(Income.date, 'YYYY-MM') == month
    ).scalar() or 0

    return {
        "month": month,
        "total_income": income,
        "total_expenses": expenses,
        "net_balance": income - expenses
    }