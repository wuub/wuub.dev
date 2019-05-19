#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "wuub"
SITENAME = "wuub.dev blog"
SITEURL = ""

PATH = "content"


THEME = "themes/brutalist"
TWITTER_USERNAME = "@wuub"
FIRST_NAME = "wuub"
MENUITEMS = [("tags", "/tags")]
LOGO = "logo.png"

TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()
DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "assets",
    "sitemap",
    "gravatar",
    "liquid_tags.img",
    "liquid_tags.video",
    "liquid_tags.youtube",
    "liquid_tags.include_code",
]

SITEMAP = {"format": "txt"}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
