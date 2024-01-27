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


CONTENT_DIR = "content/posts"


def get(name=""):

    if not name:
        raise ErrInvalidName("Please provide a post name")

    # Parse the entry file, the file should follow the following template:
    # key: value
    with open(f"{CONTENT_DIR}/{name}.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()

    hilite = CodeHiliteExtension(linenums=False, css_class="highlight")
    extras = ExtraExtension()
    md = markdown.Markdown(
        extensions=[
            "markdown_captions",
            "meta",
            "fenced_code",
            hilite,
            extras,
        ],
        output_format="html5",
    )
    html = md.convert(text)

    # Clean up the meta format
    meta = {key.lower(): value[0] for key, value in md.Meta.items()}
    summary = app.util.get_summary(html)

    if "direciton" not in meta:
        try:
            meta["direciton"] = "rtl" if langdetect.detect(summary) == "ar" else "ltr"
        except:
            meta["direciton"] = "ltr"

    if "cover" not in meta:
        meta["cover"] = app.util.get_cover(html)

    body = {"content": html, "summary": summary}

    return {**meta, **body}


def all():
    posts = []

    files = os.listdir(CONTENT_DIR)
    files.sort(key=lambda x: os.path.getmtime(CONTENT_DIR + "/" + x), reverse=True)

    for file in files:
        if file[-3:] != ".md" or file.startswith("."):
            continue

        posts.append(get(file[:-3]))

    return posts


def sort(posts):
    return sorted(posts, key=lambda i: i["date"], reverse=True)
