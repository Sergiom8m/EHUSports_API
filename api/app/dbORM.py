from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Definición de modelos
class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String, index=True)

    activities = relationship("Activity", back_populates="user")



class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    distance = Column(Float)
    init_point = Column(String)
    grade = Column(Float)
    difficulty = Column(String)
    type = Column(String)
    user_id = Column(String, ForeignKey("users.username"))

    user = relationship("User", back_populates="activities")
