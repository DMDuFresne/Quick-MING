from sqlalchemy import Table, Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
import uuid
from ..database import metadata

ingredients = Table(
    "ingredients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("uuid", String, default=lambda: str(uuid.uuid4()), unique=True, index=True),
    Column("name", String(120), nullable=False),
    Column("color", String(32), nullable=False),
    Column("uom", String(50), nullable=False),
    Column("created_on", TIMESTAMP, nullable=False, default=func.now()),
    Column("updated_on", TIMESTAMP, nullable=False, default=func.now(), onupdate=func.now()),
    Column("removed", Boolean, nullable=False, default=False),
)
