import datetime
import functools
import os
import re
import urllib
import app.views as views
from flask import (
    Flask,
    abort,
    flash,
    Markup,
    redirect,
    render_template,
    request,
    Response,
    session,
    url_for,
)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache


APP_DIR = os.path.dirname(os.path.realpath(__file__))
DEBUG = False
SECRET_KEY = "shhh, secret!"  # Used by Flask to encrypt session cookie.
SITE_WIDTH = 800


app = Flask(__name__)
app.config.from_object(__name__)

# Register the Flask apps within the main app
views.register(app)
