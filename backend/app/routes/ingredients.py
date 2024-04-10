from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..schemas.ingredient import IngredientCreate, Ingredient, IngredientUpdate
from ..operations.ingredients import (
    create_ingredient, get_ingredient, get_ingredients, 
    update_ingredient, delete_ingredient, restore_ingredient
)

router = APIRouter()


@router.post("/", response_model=Ingredient)
async def create_ingredient_route(ingredient_data: IngredientCreate):
    status, new_ingredient = await create_ingredient(ingredient_data)
    if status == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return new_ingredient


@router.get("/", response_model=List[Ingredient])
async def read_ingredients(skip: int = 0, limit: int = 100, include_removed: bool = Query(False)):
    ingredients_list = await get_ingredients(skip, limit, include_removed)
    return ingredients_list


@router.get("/{uuid}", response_model=Ingredient)
async def read_ingredient(uuid: str, include_removed: bool = Query(False)):
    status, ingredient = await get_ingredient(uuid, include_removed)
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Ingredient not found")
    elif status == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return ingredient


@router.put("/{uuid}", response_model=Ingredient)
async def update_ingredient_route(uuid: str, ingredient_data: IngredientUpdate):
    status, updated_ingredient = await update_ingredient(uuid, ingredient_data)
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Ingredient not found")
    elif status == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return updated_ingredient


@router.put("/{uuid}/remove", response_model=dict)
async def delete_ingredient_route(uuid: str):
    status, _ = await delete_ingredient(uuid)
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Ingredient not found")
    elif status == "already_processed":
        return {"message": "Ingredient was already marked as removed"}
    elif status == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return {"message": "Ingredient successfully marked as removed"}


@router.put("/{uuid}/restore", response_model=dict)
async def restore_ingredient_route(uuid: str):
    status, _ = await restore_ingredient(uuid)
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Ingredient not found")
    elif status == "already_processed":
        return {"message": "Ingredient was not marked as removed"}
    elif status == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return {"message": "Ingredient successfully restored"}

