from fastapi import FastAPI
from .api.routes import router as api_router
from .database import database

app = FastAPI(title="My Project API", version="1.0")

app.include_router(api_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()