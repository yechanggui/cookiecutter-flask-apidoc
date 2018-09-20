from flask import Blueprint
main = Blueprint('main', __name__)
from {{cookiecutter.repo_name}}.controllers.main import views

