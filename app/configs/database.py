from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app:Flask):
    db.init_app(app)
    app.db = db

    from app.models.category_model import CategoryModel
    from app.models.eisenhowers_model import EisenhowerModel
    from app.models.task_model import TaskModel
    from app.models.tasks_categories_table import tasks_categories
