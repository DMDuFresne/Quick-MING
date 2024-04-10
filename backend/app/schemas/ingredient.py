from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class IngredientBase(BaseModel):
    name: str
    color: str
    uom: str

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(IngredientBase):
    pass

class IngredientInDBBase(IngredientBase):
    uuid: UUID4
    id: Optional[int] = None
    created_on: datetime
    updated_on: datetime
    removed: bool

    class Config:
        from_attributes = True

class Ingredient(IngredientInDBBase):
    pass

class IngredientInDB(IngredientInDBBase):
    pass
