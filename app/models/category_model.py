from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import Text
from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text
from dataclasses import dataclass
from werkzeug.exceptions import NotFound

from app.exceptions.category_exceptions import CategoryAlreadyExistsError
from app.models.task_model import TaskModel

@dataclass
class CategoryModel(db.Model):
    id:int
    name:str
    description:str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    # tasks = db.relationship("TaskModel", secondary="tasks_categories", backref="categories")

    @staticmethod
    def post_validate(data):
        try:
            category = (
                CategoryModel.query.filter_by(name=data['name']).first_or_404(description="")
            )
            raise CategoryAlreadyExistsError("category already exists")
        except NotFound as e:
            ...
