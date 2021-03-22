#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Darius'
SITENAME = 'dariushall.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

# Defaults
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = False
DEFAULT_METADATA = {
    'status': 'draft',
}

FILENAME_METADATA = '(?P<title>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True