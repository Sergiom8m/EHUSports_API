from fastapi import FastAPI, HTTPException, Depends, UploadFile, status
from fastapi.responses import FileResponse
from pathlib import Path
from mimetypes import guess_extension
from typing import List, Optional
from sqlalchemy.orm import Session
from .database import get_db
from .dbORM import User, Activity
from . import crud
from .schema import *

VALID_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp']

# Inicialización de la aplicación FastAPI
app = FastAPI()

@app.get("/status")
async def read_item():
    return {"status": "VM is active"}

# Rutas de la API
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.delete("/users/{username}/", response_model=User)
def delete_user(username: str, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, username=username)


@app.get('/users/{username}/image', response_class=FileResponse)
def get_profile_image(username: str, db: Session = Depends(get_db)):
    image = crud.get_profile_image(db, username)
    if image!= None and Path(image).exists():
        return FileResponse(image, filename=Path(image).name)
    else:
        raise HTTPException(status_code=404, detail="Profile image not found")

@app.put("/users/{username}/image", tags=["Users"],
         status_code=status.HTTP_204_NO_CONTENT,
         responses={404: {"description": "User doesn't exists."}, 400: {"description": f"File is not a valid image file. Valid types: {', '.join(VALID_IMAGE_TYPES)}"}})
async def set_user_profile_image(file: UploadFile, username: str, db: Session = Depends(get_db)):
    if not (user := crud.get_user(db, username)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exists.")

    if file.content_type not in VALID_IMAGE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"File is not a valid image file. Valid types: {', '.join(VALID_IMAGE_TYPES)}")

    file_extension = guess_extension(file.content_type)
    path = f'/ehusports_api/images/{username}{file_extension}'

    if crud.set_profile_image(db, username, path):
        contents = await file.read()
        with open(path, 'wb') as f:
            f.write(contents)

@app.post("/activities/", response_model=Activity)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)

@app.get("/activities/", response_model=List[Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_activities(db, skip=skip, limit=limit)

@app.delete("/activities/{activity_id}/", response_model=Activity)
def delete_activity(activity_id: str, db: Session = Depends(get_db)):
    return crud.delete_activity(db=db, activity_id=activity_id)

@app.put("/activities/{activity_id}", response_model=Activity)
def update_activity(activity_id: str, activity: ActivityCreate, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return crud.update_activity(db, activity_id, activity)

@app.delete("/activities/", response_model=str)
def delete_all_activities(db: Session = Depends(get_db)):
    crud.delete_all_activities(db)
    return "All activities deleted successfully."

@app.delete("/users/", response_model=str)
def delete_all_users(db: Session = Depends(get_db)):
    crud.delete_all_users(db)
    return "All users deleted successfully."