from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db

tasks_categories = db.Table('tasks_categories',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('task_id', db.Integer, ForeignKey('tasks.id')),
    db.Column('category_id', db.Integer, ForeignKey('categories.id'))
)
