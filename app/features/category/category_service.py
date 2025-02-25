from app.features.category.category_repository import CategoryRepository
from app.features.category.category_model import Category
from typing import List
from uuid import UUID

class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def create(self, category: Category) -> Category:
        return self.repo.create_category(category)

    def list(self, user_id: UUID) -> List[Category]:
        return self.repo.get_categories(user_id)

    def delete(self, category_id: UUID):
        self.repo.delete_category(category_id)
