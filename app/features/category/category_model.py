from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class Category(BaseModel):
    category_id: Optional[UUID]
    user_id: UUID
    type: str
    name: str
    icon: Optional[str]
    color: Optional[str]
