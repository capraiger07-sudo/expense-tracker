from fastapi import APIRouter, Depends
from app.core.auth import get_current_user

router = APIRouter()

DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Clothing",
    "Rent",
    "EMI",
    "Bills",
    "Healthcare",
    "Education",
    "Entertainment",
    "Other"
]

custom_categories = []

@router.get("/categories")
def get_categories(current_user: str = Depends(get_current_user)):
    return DEFAULT_CATEGORIES + custom_categories

@router.post("/categories")
def add_category(name: str, current_user: str = Depends(get_current_user)):
    if name in DEFAULT_CATEGORIES + custom_categories:
        return {"message": "Category already exists"}
    custom_categories.append(name)
    return {"message": f"{name} added successfully"}