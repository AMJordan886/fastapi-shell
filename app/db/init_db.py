from app.db.session import engine
from app.db.base import Base

def init_db():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
