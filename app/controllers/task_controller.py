from flask import request, current_app, jsonify
from app.exceptions.task_exceptions import InvalidDataError, TaskAlreadyExistsError
from app.models.eisenhowers_model import EisenhowerModel
from app.models.category_model import CategoryModel
from app.models.task_model import TaskModel
from werkzeug.exceptions import NotFound

def create():
    try:
        session = current_app.db.session
        data = request.get_json()
        TaskModel.validate_post(data)
        #verificar urgency e importance para definir classificação
        eisenhower_type = TaskModel.eisenhower_type(data)
        query = EisenhowerModel.query.filter_by(type=eisenhower_type).first_or_404(description="importance and urgency must have only 1 or 2 as value")
        data['eisenhower_id'] = query.id
        #mapear categorias e verificar a existencia das mesmas
        categories = data.pop('categories')
        task = TaskModel(**data)
        for category in categories:
            try:
                category_found = CategoryModel.query.filter_by(name=category['name']).first_or_404()
                task.categories.append(category_found)
            except NotFound:
                structure = {
                    "name":category['name'],
                    "description":""
                }
                new_category = CategoryModel(**structure)
                session.add(new_category)
                session.commit()
        
        session.add(task)
        session.commit()

        task_created = {
            "id":task.id,
            "name":task.name,
            "description":task.description,
            "duration":task.duration,
            "importance":task.importance,
            "urgency":task.urgency,
            "eisenhower_id":task.eisenhower_id,
            "categories":task.categories
        }

        return jsonify(task_created), 201
    except (NotFound, TaskAlreadyExistsError) as e:
        if type(e).__name__ == "TaskAlreadyExistsError":
            return {"error":str(e)}, 409
        
        if type(e).__name__ == "NotFound":
            return {"error":e.description}, 404

def get_all():
    query = (
        TaskModel.query.all()
    )

    tasks_found = [
        {
            "id":task.id,
            "name":task.name,
            "description":task.description,
            "duration":task.duration,
            "importance":task.importance,
            "urgency":task.urgency,
            "eisenhower_id":task.eisenhower_id,
            "categories":task.categories
        } for task in query]

    return jsonify(tasks_found), 200

def update(task_id):
    session = current_app.db.session
    data = request.get_json()
    try:
        task = TaskModel.query.get_or_404(task_id, description="task not found to be updated")

        for key, value in data.items():
            setattr(task, key, value)

        aux = {
            "urgency":task.urgency,
            "importance":task.importance
        }

        eisenhower_type = TaskModel.eisenhower_type(aux)
        query = EisenhowerModel.query.filter_by(type=eisenhower_type).first_or_404(description="importance and urgency must have only 1 or 2 as value")
        task.eisenhower_id = query.id

        session.add(task)
        session.commit()

        task_updated = {
            "id":task.id,
            "name":task.name,
            "description":task.description,
            "duration":task.duration,
            "importance":task.importance,
            "urgency":task.urgency,
            "eisenhower_id":task.eisenhower_id,
            "categories":task.categories
        }

        return jsonify(task_updated), 200    
    except (NotFound, TaskAlreadyExistsError) as e:
        if type(e).__name__ == "TaskAlreadyExistsError":
            return {"error":str(e)}, 409
        
        if type(e).__name__ == "NotFound":
            return {"error":e.description}, 404

def delete(task_id):
    session = current_app.db.session
    try:
        task = TaskModel.query.get_or_404(task_id, description="task not found to be deleted")
        session.delete(task)
        session.commit()
        return "", 204
    except NotFound as e:
        return {"error":e.description}, 404