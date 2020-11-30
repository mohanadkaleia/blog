import markdown
import markdown.extensions.fenced_code
import os
import re

from bs4 import BeautifulSoup
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension


class ErrNotFound(Exception):
	pass


class ErrInvalidFormat(Exception):
	pass

class ErrInvalidName(Exception):
	pass


CONTENT_DIR = 'content/books'


def get(name=""):		
	if not name:
		raise ErrInvalidName('Please provide a book name')

	# Parse the entry file, the file should follow the following template:
	# key: value	
	with open(f"{CONTENT_DIR}/{name}.md", "r", encoding="utf-8") as input_file:
		text = input_file.read()
	
	hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
	extras = ExtraExtension()
	md = markdown.Markdown(extensions=['meta', 'fenced_code', hilite, extras], output_format='html5')	
	html = md.convert(text)
		
	meta = {key: value[0] for key, value in md.Meta.items()}
	body = {'content': html}

	return {**meta, **body}

def all():
	books = []
	
	files = os.listdir(CONTENT_DIR)

	for file in files:
		
		if file[-3:] != '.md':
			continue
		
		books.append(get(file[:-3]))

	return books
