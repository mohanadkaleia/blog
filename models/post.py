import markdown
import markdown.extensions.fenced_code
import os

from bs4 import BeautifulSoup
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension


class ErrNotFound(Exception):
	pass


class ErrInvalidFormat(Exception):
	pass

class ErrInvalidName(Exception):
	pass


CONTENT_DIR = 'content/posts'

def get(name=""):		
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

	return {
		'meta': meta, 
		'content': html,
	}	

def all():
	return os.listdir(CONTENT_DIR)
