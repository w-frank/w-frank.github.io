#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Frank'
SITENAME = 'The Game of Logic'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%A %d %B %Y'
DEFAULT_LANG = 'en'

STATIC_PATHS = ['CNAME']

EXTRA_PATH_METADATA = {
    ... other extra path metadata ...
    'CNAME': {'path': 'CNAME'},
}

# Specify a customized theme, via path relative to the settings file
THEME = "theme/cebong"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
