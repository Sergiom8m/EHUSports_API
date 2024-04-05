from pydantic import BaseModel

# Definición de modelos Pydantic para la validación de datos
class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):

    class Config:
        orm_mode = True

class ActivityBase(BaseModel):
    id: str
    name: str
    distance: float
    init_point: str
    grade: float
    difficulty: str
    type: str
    user_id: str

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):

    class Config:
        orm_mode = True

