from sqlalchemy.orm import backref, relationship, validates
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.exceptions import NotFound
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Text

from app.exceptions.task_exceptions import InvalidDataError, TaskAlreadyExistsError


@dataclass
class TaskModel(db.Model):
    id:int
    name:str
    description:str
    duration:int
    importance:int
    urgency:int
    eisenhower_id: int

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(
        Integer,
        ForeignKey('eisenhowers.id')
    )

    eisenhower = db.relationship("EisenhowerModel", backref="tasks")
    categories = db.relationship("CategoryModel", secondary="tasks_categories", backref="tasks")

    @staticmethod
    def validate_post(data):
        try:
            task = (
                TaskModel.query.filter_by(name=data['name']).first_or_404(description="")
            )
            raise TaskAlreadyExistsError("task already exists")
        except NotFound as e:
            ...

    @staticmethod
    def eisenhower_type(data):
        urgency = data['urgency']
        importance = data['importance']

        if urgency == 1 and importance == 1:
            return str('Do It First')
    
        if urgency == 1 and importance == 2:
            return str('Schedule It')
        
        if urgency == 2 and importance == 1:
            return str('Delegate It')
        
        if urgency == 2 and importance == 2:
            return str('Delete It')
