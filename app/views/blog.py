import flask
import models.post


from flask import Blueprint, render_template, Markup
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache

app = Blueprint('blog', __name__, url_prefix='/')

# Configure micawber with the default OEmbed providers (YouTube, Flickr, etc).
# We'll use a simple in-memory cache so that multiple requests for the same
# video don't require multiple network requests.
oembed_providers = bootstrap_basic(OEmbedCache())

@app.route('/')
def index():
	posts = models.post.all()
	return render_template('index.html', posts=posts)

@app.route('/<slug>')
def post(slug):
	entry = models.post.get(slug)	
	content = parse_html(
		entry['content'],
		oembed_providers,
		urlize_all=True,
	)	
	return render_template('article.html', post=Markup(content), meta=entry['meta'])


@app.route('/contact')
def contact():
	return 'mohanad@kaleia.io'
	
