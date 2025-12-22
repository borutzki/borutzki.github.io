"""Create new post in _posts` location, with timestamps in place and title slugified to match URL paths.

Example usage:
python3 ./newpost.py "How to check whether Python script has elevated privileges?"

"""

import pathlib
import datetime
import re
import sys
import unicodedata

ARTICLE_TEMPLATE = """---
layout: post
title:  ""
excerpt_separator: <!--more-->
---

<!--more-->
"""
POSTS = pathlib.Path(__file__).parent / "_posts"


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def create_file_name(title: str | None) -> str:
    """Returns normalized name of a file based on provided title"""
    date = str(datetime.date.today())
    if title:
        normalized_title = slugify(title)
        return f"{date}-{normalized_title}"
    else:
        return date


def create_new_post_file(filename: str) -> None:
    """Create new Markdown file in default location with default template."""
    with open(POSTS / f"{filename}.md", mode="w") as md:
        md.write(ARTICLE_TEMPLATE)


if __name__ == "__main__":
    try:
        title = sys.argv[1]
    except IndexError:
        title = None

    filename = create_file_name(title)
    create_new_post_file(filename)
