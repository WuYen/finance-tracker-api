from app.core.config import supabase
from app.features.category.category_model import Category
from typing import List, Optional
from uuid import UUID

class CategoryRepository:
    @staticmethod
    def create_category(category: Category) -> Category:
        data = supabase.table("category").insert(category.dict()).execute()
        return Category(**data.data[0])

    @staticmethod
    def get_categories(user_id: UUID) -> List[Category]:
        data = supabase.table("category").select("*").eq("user_id", str(user_id)).execute()
        return [Category(**cat) for cat in data.data]

    @staticmethod
    def delete_category(category_id: UUID):
        supabase.table("category").delete().eq("category_id", str(category_id)).execute()
