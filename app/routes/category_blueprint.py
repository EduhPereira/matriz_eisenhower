from flask import Blueprint
from app.controllers.category_controller import create, delete, get_all, update, delete

bp = Blueprint("bp_category", __name__, url_prefix="/category")

bp.post("")(create)
bp.get("")(get_all)
bp.patch("/<int:category_id>")(update)
bp.delete("/<int:category_id>")(delete)
