from flask import Flask
from cache import cache
from api import api

app = Flask(__name__)

cache.init_app(app)
app.register_blueprint(api)
