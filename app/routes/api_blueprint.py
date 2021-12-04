from flask import Blueprint
from app.routes.category_blueprint import bp as bp_category
from app.routes.task_blueprint import bp as bp_task

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_category)
bp_api.register_blueprint(bp_task)
