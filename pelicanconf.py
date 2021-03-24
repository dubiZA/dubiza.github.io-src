#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Darius'
SITENAME = 'Darius Hall'
SITEURL = 'http://localhost:8000/'

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

STATIC_PATHS = ['images/', 'extra/robots.txt', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'feed_summary']

# Theme config
THEME = 'themes/Flex'
SITELOGO = '/images/profile.jpg'
SITETITLE = 'Darius Hall'
SITESUBTITLE = 'My piece of the Internet'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

MAIN_MENU = True
MENUITEMS = (
    ('Categories', '/categories'),
    ('Tags', '/tags')
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/dariushall/'),
          ('GitHub', 'https://github.com/dubiZA'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True