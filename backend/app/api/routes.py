from fastapi import APIRouter
from ..routes.ingredients import router as ingredient_router

router = APIRouter()

router.include_router(ingredient_router, prefix="/ingredients", tags=["ingredients"])
