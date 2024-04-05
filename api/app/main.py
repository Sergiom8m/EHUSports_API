from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from .database import get_db
from .dbORM import User, Activity
from . import crud
from .schema import *

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Rutas de la API
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/users/", response_model=User)
def delete_user(username: str, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, username=username)

@app.post("/activities/", response_model=Activity)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)

@app.get("/activities/", response_model=List[Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_activities(db, skip=skip, limit=limit)

@app.post("/activities/", response_model=Activity)
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    return crud.delete_activity(db=db, activity_id=activity_id)