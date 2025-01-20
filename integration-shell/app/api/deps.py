from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal, engine

from app.models.item import Base, Item
from app.models.integration_log import Base, IntegrationLog

# Crear las tablas en la base de datos
# Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

