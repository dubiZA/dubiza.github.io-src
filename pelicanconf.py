#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'Darius'
SITEURL = 'http://localhost:8000'
SITENAME = 'Darius Hall'
SITETITLE = 'Darius Hall'
SITESUBTITLE = 'My piece of the Internet'
SITEDESCRIPTION = 'The epic chronicles of Darius\' forays in to tech, coding and, well, all the things'
SITELOGO = SITEURL + '/images/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = 'themes/Flex'
PATH = 'content'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'America/Denver'

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['./pelican-plugins']
# PLUGINS = ['sitemap', 'feed_summary']

DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/dariushall/'),
    ('github', 'https://github.com/dubiZA'),
    ('rss', '/blog/feeds/all.atom.xml'),
)

MENUITEMS = (
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags')
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa',
    'icon': False,
    'language': 'en_US',
}

COPYRIGHT_YEAR = datetime.now().strftime('%Y')
DEFAULT_PAGINATION = False

# DISQUS_SITENAME = ''
# ADD_THIS_ID = ''

STATIC_PATHS = ['images/', 'extra/robots.txt', 'extra/favicon.ico', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

CUSTOM_CSS = 'static/custom.css'

# Other Defaults
DEFAULT_DATE = 'fs'
DEFAULT_METADATA = {
    'status': 'draft',
}

FILENAME_METADATA = '(?P<title>.*)'

# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.6,
#         'indexes': 0.6,
#         'pages': 0.5,
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly',
#     }
# }

USE_FOLDER_AS_CATEGORY = True

# Blogroll
LINKS = (
    ('AWS', '/category/aws'),
    ('Pelican', 'https://getpelican.com/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True