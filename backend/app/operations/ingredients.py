import uuid
from sqlalchemy.sql import select, update
from ..models.ingredients import ingredients
from ..schemas.ingredient import IngredientCreate, IngredientUpdate
from ..database import database


async def create_ingredient(ingredient_data: IngredientCreate):
    new_uuid = str(uuid.uuid4())
    try:
        query = ingredients.insert().values(uuid=new_uuid, removed=False, **ingredient_data.dict(exclude_unset=True))
        await database.execute(query)
        return "success", await get_ingredient(new_uuid)
    except Exception as e:
        print(e)
        return "error", None


async def get_ingredients(skip: int = 0, limit: int = 100, include_removed: bool = False):
    try:
        if include_removed:
            query = select(ingredients).offset(skip).limit(limit)
        else:
            query = select(ingredients).where(ingredients.c.removed == False).offset(skip).limit(limit)
        results = await database.fetch_all(query)
        return results
    except Exception as e:
        print(e)
        return []


async def get_ingredient(ingredient_uuid: str, include_removed: bool = False):
    conditions = [ingredients.c.uuid == ingredient_uuid]
    if not include_removed:
        conditions.append(ingredients.c.removed == False)
    query = select(ingredients).where(*conditions)
    try:
        result = await database.fetch_one(query)
        if result:
            return "success", result
        else:
            return "not_found", None
    except Exception as e:
        print(e)
        return "error", None


async def update_ingredient(ingredient_uuid: str, ingredient_data: IngredientUpdate):
    try:
        query = update(ingredients).where(
            ingredients.c.uuid == ingredient_uuid, ingredients.c.removed == False
        ).values(**ingredient_data.dict(exclude_unset=True))
        result = await database.execute(query)
        if result:
            return "success", await get_ingredient(ingredient_uuid)
        else:
            return "not_found", None
    except Exception as e:
        print(e)
        return "error", None


async def delete_ingredient(ingredient_uuid: str):
    try:
        existing_ingredient = await get_ingredient(ingredient_uuid)
        if existing_ingredient[0] == "not_found":
            return "not_found", None
        query = update(ingredients).where(ingredients.c.uuid == ingredient_uuid).values(removed=True)
        await database.execute(query)
        return "success", None
    except Exception as e:
        print(e)
        return "error", None


async def restore_ingredient(ingredient_uuid: str):
    try:
        existing_ingredient = await get_ingredient(ingredient_uuid, include_removed=True)
        if existing_ingredient[0] == "not_found":
            return "not_found", None
        if existing_ingredient[1].removed == False:
            return "already_processed", None
        query = update(ingredients).where(ingredients.c.uuid == ingredient_uuid).values(removed=False)
        await database.execute(query)
        return "success", None
    except Exception as e:
        print(e)
        return "error", None

