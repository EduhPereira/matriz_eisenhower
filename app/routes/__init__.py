from flask import Blueprint, Flask
from app.routes.api_blueprint import bp_api

def init_app(app:Flask):
    app.register_blueprint(bp_api)
