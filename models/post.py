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
	summary = get_summary(html)
	body = {'content': html, 'summary': summary}

	return {**meta, **body}

def all():
	posts = []
	
	files = os.listdir(CONTENT_DIR)

	for file in files:
		
		if file[-3:] != '.md':
			continue
		
		posts.append(get(file[:-3]))

	return posts


# This function is forked from here: https://github.com/MinchinWeb/minchin.pelican.plugins.summary
def get_summary(content):
	# Summary will take the first paragraph of the content
	begin_marker, end_marker = '<p>', '</p>'
	remove_markers = False
	begin_summary = content.find(begin_marker)
	end_summary = content.find(end_marker)

	summary = content[begin_summary:end_summary]
	summary = re.sub(r"<div.*>", "", summary)
	summary = re.sub(r"</div>", "", summary)

	return summary
