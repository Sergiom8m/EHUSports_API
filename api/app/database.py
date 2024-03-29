from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

POSTGRES_USER = environ['POSTGRES_USER']
POSTGRES_PASSWORD = environ['POSTGRES_PASSWORD']
POSTGRES_IP = environ['POSTGRES_IP']
POSTGRES_DB = environ['POSTGRES_DB']

# Configuración de la base de datos
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_IP}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
