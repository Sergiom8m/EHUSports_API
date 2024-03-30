from .dbORM import User, Activity
from .schema import UserCreate, ActivityCreate
from typing import Optional
from sqlalchemy.orm import Session


# Métodos CRUD para usuarios
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Métodos CRUD para actividades deportivas
def get_activity(db: Session, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Activity).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activities_by_user(db: Session, user_id: Optional[str] = None, skip: int = 0, limit: int = 100):
    if user_id:
        return db.query(Activity).filter(Activity.user_id == user_id).offset(skip).limit(limit).all()
    else:
        return db.query(Activity).offset(skip).limit(limit).all()

def get_activities_by_type_and_user(db: Session, activity_type: str, user_id: Optional[str] = None, skip: int = 0, limit: int = 100):
    if user_id:
        return db.query(Activity).filter(Activity.user_id == user_id, Activity.type == activity_type).offset(skip).limit(limit).all()
    else:
        return db.query(Activity).filter(Activity.type == activity_type).offset(skip).limit(limit).all()
    
def get_activities_by_type(db: Session, activity_type: str, skip: int = 0, limit: int = 100):
    return db.query(Activity).filter(Activity.type == activity_type).offset(skip).limit(limit).all()