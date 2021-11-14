from flask import Flask
from .api.routes import api
from .site.routes import site

app = Flask(__name__)

app.config.from_object(Config)