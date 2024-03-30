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

@app.get("/users/{username}", response_model=User)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/activities/", response_model=Activity)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)

@app.get("/activities/", response_model=List[Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_activities(db, skip=skip, limit=limit)

@app.get("/{user_id}/activities", response_model=List[Activity])
def read_activities_by_user(user_id: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = crud.get_activities_by_user(db, user_id=user_id, skip=skip, limit=limit)
    if not activities:
        raise HTTPException(status_code=404, detail=f"No activities found for user with ID {user_id}")
    return activities

@app.get("/{user_id}/activities/type/{activity_type}", response_model=List[Activity])
def read_activities_by_type(activity_type: str, user_id: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if user_id:
        activities = crud.get_activities_by_type_and_user(db, activity_type=activity_type, user_id=user_id, skip=skip, limit=limit)
    else:
        activities = crud.get_activities_by_type(db, activity_type=activity_type, skip=skip, limit=limit)
    return activities

@app.get("/activities/{activity_id}", response_model=Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity