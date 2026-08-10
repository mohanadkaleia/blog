"""One-off cleanup of Pandoc/WordPress residue left by the migration off WordPress.

The old export wrapped text in Pandoc attribute blocks -- `[text]{style="..."}`,
`![img](src){.aligncenter width="300"}`, ```` ```{=html} ```` separators. Python-Markdown
does not implement Pandoc's bracketed-span syntax, so all of it rendered as
literal text in the middle of the prose.

Presentation is dropped (the stylesheet handles it); meaning is kept -- underline
becomes <u>, an inline direction override becomes <span dir="...">, and the
colour-coded section titles in the Caffe post become real headings.

Only prose is touched: lines inside fenced code blocks are left byte-for-byte
alone, so the CSS and HTML tutorials keep their sample code.
"""

import glob
import re

# Attribute blocks the exporter produced. Anything not matching these -- `{ lr_mult: 1 }`,
# `{REQUEST_FILENAME}`, `{config.server['url']}` -- is real content and is left alone.
WP_CLASSES = (
    r"aligncenter|alignleft|alignright|size-\w+|wp-image-\d+|underline|"
    r"prettyprint|prettyprinted|western|lang-[\w+-]+|author-d-\w+"
)
ATTRS = (
    r'(?:\s*(?:style="[^"]*"|dir="[^"]*"|width="[^"]*"|height="[^"]*"'
    rf'|usually-unique-id="[^"]*"|#[\w-]+|\.(?:{WP_CLASSES})))+'
)

SPAN = re.compile(r"\[([^\]\n]*)\]\{(" + ATTRS + r")\s*\}")
IMAGE = re.compile(r"(!\[[^\]\n]*\]\([^)\n]*\))\{" + ATTRS + r"\s*\}")
BARE = re.compile(r"\{" + ATTRS + r"\s*\}")
EMPTY = re.compile(r"\{\s*\}")

UNDERLINE = re.compile(r"\.underline|text-decoration:\s*underline")
DIR = re.compile(r'dir="(\w+)"')

FENCE = re.compile(r"^\s*(?:```|~~~)")
FENCE_STYLE = re.compile(r'\s*style="[^"]*"')
# Pandoc emits ```{=html}\n<!-- -->\n``` purely to break adjacent lists apart. The
# comment has to stay: it is what stops the indented block that follows from being
# absorbed into the list above, which would strip it of its code formatting.
HTML_SEPARATOR = re.compile(r"^\s*```\{=html\}\n(\s*<!-- -->)\n\s*```", re.MULTILINE)


def unwrap_span(match):
    text, attrs = match.group(1), match.group(2)

    if not text.strip():
        return text

    if UNDERLINE.search(attrs):
        return f"<u>{text}</u>"

    direction = DIR.search(attrs)
    if direction:
        return f'<span dir="{direction.group(1).lower()}">{text}</span>'

    # Colour, font-size and font-family are the stylesheet's business now.
    return text


def clean_line(line):
    # `{}` is deliberately not touched here. Several posts keep their code in
    # indented blocks rather than fences, so this runs over real Go and protobuf
    # -- and `&server{}` is code, not a leftover attribute block.
    cleaned = SPAN.sub(unwrap_span, line)
    cleaned = IMAGE.sub(r"\1", cleaned)
    cleaned = BARE.sub("", cleaned)

    # Only tidy trailing space on lines we actually rewrote; indented code is
    # cleaned too and its whitespace is not ours to touch.
    return re.sub(r"[ \t]+$", "", cleaned) if cleaned != line else line


def clean(text):
    text = HTML_SEPARATOR.sub(r"\1", text)

    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            # The opening fence carries its own attribute block, e.g.
            # ``` {.lang-php dir="ltr" style="..."}. Markdown >= 3.4 forwards that
            # style= to Pygments, which already sets one, and raises TypeError.
            # Drop only the style: the language class and dir= still do real work.
            if not in_fence and 'style="' in line:
                line = EMPTY.sub("", FENCE_STYLE.sub("", line)).rstrip()
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(line if in_fence else clean_line(line))

    return "\n".join(out)


# `::: {dir="rtl"}` ... `:::` is a Pandoc fenced div. Python-Markdown has no such
# syntax, so the markers printed as literal text. Note `:::python` is excluded --
# that is CodeHilite's language shebang and is handled separately below.
# The `>` allows for a div Pandoc opened inside a blockquote.
DIV_FENCE = re.compile(r"^>?[ \t]*:::+[ \t]*(?:\{[^}]*\})?[ \t]*$")
# Pandoc also wrapped blocks in a bare <div>. Markdown does not process markdown
# inside a raw HTML block, which is why the image in forbidden.md rendered as
# literal `![](...)` text instead of an <img>.
BARE_DIV = re.compile(r"^</?div>\s*$")
SHEBANG = re.compile(r"^:::(\w+)\s*$")


def strip_pandoc_blocks(text):
    lines = text.split("\n")
    out, in_fence, skip_next = [], False, False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        if FENCE.match(line):
            # A ```-fence followed by `:::python` leaves the shebang visible inside
            # the code block; move the language onto the fence where it belongs.
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not in_fence and SHEBANG.match(nxt) and not line.strip().rstrip("`~"):
                line = line.rstrip() + SHEBANG.match(nxt).group(1)
                skip_next = True
            in_fence = not in_fence
            out.append(line)
            continue

        # An indented `:::python` is a real CodeHilite shebang on an indented code
        # block and must survive; only column-zero markers are Pandoc's.
        if not in_fence and (DIV_FENCE.match(line) or BARE_DIV.match(line)):
            continue

        out.append(line)

    return "\n".join(out)


def main():
    changed = 0
    for path in sorted(glob.glob("content/posts/*.md")):
        before = open(path, encoding="utf-8").read()
        after = strip_pandoc_blocks(clean(before))
        if after != before:
            open(path, "w", encoding="utf-8").write(after)
            changed += 1
            print(f"cleaned {path}")
    print(f"\n{changed} files changed")


if __name__ == "__main__":
    main()
