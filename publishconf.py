#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Frank'
SITENAME = 'WILL FRANK'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
# DEFAULT_DATE_FORMAT = '%A %d %B %Y'
DEFAULT_LANG = 'en'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'html',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'html/projects.html': {'path': 'projects.html'},
}

# Specify a customized theme, via path relative to the settings file
THEME = "theme/minimalist"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

CATEGORIES = (('blog'), ('test'))

# Disqus Comments
DISQUS_SITENAME = 'willfrank-co-uk'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Blog', '/'),
    ('Portfolio', '/pages/portfolio.html'),
    ('About', '/pages/about.html')
)


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
