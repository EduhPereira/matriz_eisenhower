from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer

class EisenhowerModel(db.Model):
    id:int
    type:str

    __tablename__ = 'eisenhowers'

    id = Column(Integer, primary_key=True)
    type = Column(String(100))
