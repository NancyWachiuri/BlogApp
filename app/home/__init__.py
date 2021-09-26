from flask import Blueprint
from . import views, errors

home = Blueprint('home',__name__)