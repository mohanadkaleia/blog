#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mohanad Kaleia'
SITENAME = 'Mohanad Kaleia'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Pacific'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('twitter', 'https://twitter.com/m_kaleia'),
         ('github', 'https://github.com/mohanadkaleia'),
         ('LinkedIn', 'https://www.linkedin.com/in/mohanad-kaleia-077a8368/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 0
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['summary', 'clean_summary']