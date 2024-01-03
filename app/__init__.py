import os
import app.views as views
from flask import (
    Flask,
)


APP_DIR = os.path.dirname(os.path.realpath(__file__))
DEBUG = False
SECRET_KEY = "shhh, secret!"  # Used by Flask to encrypt session cookie.
SITE_WIDTH = 800


app = Flask(__name__)
app.config.from_object(__name__)

# Register the Flask apps within the main app
views.register(app)
