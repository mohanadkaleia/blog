import markdown
import markdown.extensions.fenced_code
import os
import unicodedata
import app.util
import app.logger as logger

from datetime import datetime
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

# Every format that has ever shown up in a `Date:` header. Ordered most common
# first; parse_date walks the list and takes the first one that sticks.
DATE_FORMATS = (
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
    "%b %d, %Y",
    "%B %d, %Y",
)

# A post is rendered right-to-left once this share of its letters is RTL script.
# Well below 0.5 so that Arabic posts carrying Latin code blocks still count.
RTL_THRESHOLD = 0.25


def parse_date(value):
    # Fall back to the epoch rather than blowing up: a post with a broken date
    # header should sink to the bottom of the list, not take the page down.
    text = (value or "").strip()

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue

    log.warning(f"Could not parse date '{text}', falling back to epoch")
    return datetime.min


def detect_direction(html):
    # Unicode tags every character with a bidirectional class; 'R' and 'AL' are
    # exactly the right-to-left ones (Hebrew and Arabic script respectively).
    text = BeautifulSoup(html, "html.parser").get_text()
    letters = [char for char in text if char.isalpha()]

    if not letters:
        return "ltr"

    rtl = sum(1 for char in letters if unicodedata.bidirectional(char) in ("R", "AL"))

    return "rtl" if rtl / len(letters) >= RTL_THRESHOLD else "ltr"


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

    # An explicit `Direction:` header always wins over what we detect.
    if "direction" not in meta:
        meta["direction"] = detect_direction(html)

    if "cover" not in meta:
        meta["cover"] = app.util.get_cover(html)

    date = parse_date(meta.get("date"))
    body = {
        "content": html,
        "summary": summary,
        "date": date.strftime("%b %d, %Y"),
        "date_obj": date,
        "date_iso": date.strftime("%Y-%m-%d"),
    }

    return {**meta, **body}


def all():
    posts = []

    for file in os.listdir(CONTENT_DIR):
        if file[-3:] != ".md" or file.startswith("."):
            continue

        posts.append(get(file[:-3]))

    # Sort on the `Date:` header, not the file's mtime: a fresh git clone stamps
    # every file with the checkout time, which made the order arbitrary on deploy.
    return sort(posts)


def sort(posts):
    return sorted(posts, key=lambda i: i["date_obj"], reverse=True)
