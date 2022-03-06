#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Frank'
SITENAME = 'Will Frank'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%-d %B %Y'
DEFAULT_LANG = 'en'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'html/projects.html': {'path': 'projects.html'}
}

# Specify a customized theme, via path relative to the settings file
THEME = "theme/minimalist"
THEME_STATIC_DIR = 'static'

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disqus Comments
DISQUS_SITENAME = 'willfrank-co-uk'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (
    ('Blog', '/'),
    ('Portfolio', '/pages/portfolio.html'),
    ('About', '/pages/about.html')
)

READERS = {'html': None}

#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.tables':{},
#}
#    }

#from markdown.extensions.tables import TableExtension
#MARKDOWN = {
#    "extensions": [TableExtension()]    
#}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
