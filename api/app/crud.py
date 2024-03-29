from .dbORM import User, Activity
from .schema import UserCreate, ActivityCreate
from sqlalchemy.orm import Session

# Métodos CRUD para usuarios
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email)
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
    db_activity = Activity(name=activity.name, description=activity.description)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity