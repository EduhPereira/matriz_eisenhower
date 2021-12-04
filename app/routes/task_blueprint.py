from flask import Blueprint
from app.controllers.task_controller import create, get_all, update, delete

bp = Blueprint("bp_task", __name__, url_prefix="/task")

bp.post("")(create)
bp.get("")(get_all)
bp.patch("<int:task_id>")(update)
bp.delete("<int:task_id>")(delete)