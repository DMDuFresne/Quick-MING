from databases import Database
from sqlalchemy import create_engine, MetaData
from .config import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()