import markdown
import markdown.extensions.fenced_code
import os
import app.util
import app.logger as logger
import langdetect

from bs4 import BeautifulSoup
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension

log = logger.get_logger(__name__)


class ErrNotFound(Exception):
	pass


class ErrInvalidFormat(Exception):
	pass

class ErrInvalidName(Exception):
	pass


CONTENT_DIR = 'content/posts'


def get(name=""):		
	log.info (f'Get article: {name}')

	if not name:		
		raise ErrInvalidName('Please provide a post name')

	# Parse the entry file, the file should follow the following template:
	# key: value	
	with open(f"{CONTENT_DIR}/{name}.md", "r", encoding="utf-8") as input_file:
		text = input_file.read()
	
	hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
	extras = ExtraExtension()
	md = markdown.Markdown(extensions=['meta', 'fenced_code', hilite, extras], output_format='html5')	
	html = md.convert(text)
		
	# Clean up the meta format
	meta = {key: value[0] for key, value in md.Meta.items()}
	summary = app.util.get_summary(html)	
	
	if 'direciton' not in meta:
		try:
			meta['Direction'] = 'rtl' if langdetect.detect(summary) == 'ar' else 'ltr'			
		except:
			meta['Direction'] = 'ltr'
	
	body = {'content': html, 'summary': summary}

	return {**meta, **body}

def all():
	log.info ('Get all articles')

	posts = []
	
	files = os.listdir(CONTENT_DIR)

	for file in files:
		
		if file[-3:] != '.md' or file.startswith('.'):
			continue
		
		posts.append(get(file[:-3]))

	return sort(posts)


def sort(posts):
	return sorted(posts, key = lambda i: i['date'], reverse=True)