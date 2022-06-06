from datetime import datetime
from flask import Blueprint
from cache import cache

api = Blueprint('api', __name__)

@api.route("/")
@cache.cached(timeout=10)
def index():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")