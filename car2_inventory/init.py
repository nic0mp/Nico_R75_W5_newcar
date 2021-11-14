from flask import Flask
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(auth)

app.config.from_object(Config)