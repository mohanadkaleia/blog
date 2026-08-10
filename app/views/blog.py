import flask
import app.models.post as post_model
import config as cfg
import app.logger as logger

from flask import Blueprint, render_template, Markup
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache

app = Blueprint("blog", __name__, url_prefix="/")
log = logger.get_logger(__name__)
config = cfg.get_config()

# Configure micawber with the default OEmbed providers (YouTube, Flickr, etc).
# We'll use a simple in-memory cache so that multiple requests for the same
# video don't require multiple network requests.
oembed_providers = bootstrap_basic(OEmbedCache())


@app.route("/")
def index():
    log.info("Request the main page")
    posts = post_model.all()
    return render_template("home.html", posts=posts, config=config)


@app.route("/blog")
def blog():
    log.info("Request /blog")
    posts = post_model.all()
    return render_template("blog.html", posts=posts, config=config)


@app.route("/<slug>")
def post(slug):
    log.info(f"Request /{slug}")

    try:
        entry = post_model.get(slug)
    except Exception:
        # Status matters: /books used to be a real page, so it needs to answer
        # with a genuine 404 now rather than a 200 that says "not found".
        return "oops.. I could not find this page!!", 404

    content = parse_html(
        entry["content"],
        oembed_providers,
        urlize_all=True,
    )
    entry["content"] = Markup(content)
    return render_template("article.html", post=entry, config=config)


@app.route("/contact")
def contact():
    log.info("Request /contact")
    return "mohanadkaleia@gmail.com"


@app.route("/mentorship")
def mentorship():
    return "If you are undergrad or junior software engineer and need a mentor, feel free to shoot me an email mohanad.kaleia[at]gmail[dot]com ✌️"
