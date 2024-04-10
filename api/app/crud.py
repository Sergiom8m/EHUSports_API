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

def delete_user(db: Session, username: str):
    db_user = db.query(User).filter(User.username == username).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_profile_image(db: Session, username: str) -> bool:
    result = db.query(User.profile_image).filter(User.username == username).first()
    return result.profile_image if result else result

def set_profile_image(db: Session, username: str, path: str) -> bool:
    if user := get_user(db, username):
        user.profile_image = path
        db.commit()
        db.refresh(user)
        return True
    return False

# Métodos CRUD para actividades deportivas

def get_activity(db: Session, activity_id: str):
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Activity).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: ActivityCreate):
    db_activity = Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def delete_activity(db: Session, activity_id: str):
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    db.delete(db_activity)
    db.commit()
    return db_activity


def update_activity(db: Session, activity_id: str, activity: ActivityCreate):
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    db_activity.name = activity.name
    db_activity.distance = activity.distance
    db_activity.init_point = activity.init_point
    db_activity.grade = activity.grade
    db_activity.difficulty = activity.difficulty
    db_activity.type = activity.type
    db.commit()
    db.refresh(db_activity)
    return db_activity

def delete_all_activities(db: Session):
    db.query(Activity).delete()
    db.commit()
    
def delete_all_users(db:Session):
    db.query(User).delete()
    db.commit()