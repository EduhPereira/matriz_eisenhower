from flask import request, current_app, jsonify
from app.models.category_model import CategoryModel
from werkzeug.exceptions import NotFound
from app.exceptions.category_exceptions import CategoryAlreadyExistsError

def create():
    session = current_app.db.session
    data = request.get_json()
    try:
        category = CategoryModel(**data)
        session.add(category)
        session.commit()
        return jsonify(category), 201
    except CategoryAlreadyExistsError as e:
        return {"error":str(e)}, 409

def get_all():
    query = (
        CategoryModel.query.all()
    )

    categories_found = [
        {
            "id":category.id,
            "name":category.name,
            "description":category.description,
            "tasks":category.tasks
        } for category in query
    ]
    return jsonify(categories_found)

def update(category_id):
    session = current_app.db.session
    data = request.get_json()
    try:
        category = CategoryModel.query.get_or_404(category_id, description="category not found to be updated")
        for key, value in data.items():
            setattr(category, key, value)

        session.add(category)
        session.commit()

        return jsonify(category), 200    
    except NotFound as e:
        return {"error":e.description}, 404

def delete(category_id):
    session = current_app.db.session
    try:
        category = CategoryModel.query.get_or_404(category_id, description="category not found to be deleted")
        session.delete(category)
        session.commit()
        return "", 204
    except NotFound as e:
        return {"error":e.description}, 404
