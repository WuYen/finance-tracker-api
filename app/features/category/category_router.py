from fastapi import APIRouter, HTTPException
from app.features.category.category_service import CategoryService
from app.features.category.category_model import Category
from typing import List
from uuid import UUID

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()

@router.post("/", response_model=Category)
def create_category(category: Category):
    return service.create(category)

@router.get("/{user_id}", response_model=List[Category])
def get_categories(user_id: UUID):
    return service.list(user_id)

@router.delete("/{category_id}")
def delete_category(category_id: UUID):
    service.delete(category_id)
    return {"status": "deleted"}
