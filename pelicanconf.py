#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Brian Mc Donald'
SITENAME = 'Brian Mc Donald'
SITEURL = 'https://brianmcdonald.me' #https://brianmcdonald.github.io/brianmcdonald.me/'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_IE'
LOCALE = 'en_IE'
OUTPUT_PATH = 'docs/'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Writing', '/#writing'),)

# Social widget
SOCIAL = (
    ('rss', 'feeds/all.atom.xml'),
    ('github', 'https://github.com/brianmcdonald'),
    ('linkedin', 'https://www.linkedin.com/in/brian-mc-donald-1b8a4013/'),
)
DEFAULT_PAGINATION = False

# Mostly Brian's additions
PLUGINS = ['minchin.pelican.plugins.post_stats','similar_posts']
DEFAULT_CATEGORY = 'General'
TYPOGRIFY = True
THEME = 'themes/brian'
THEME_STATIC_DIR = 'theme'
RELATIVE_URLS = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10
ROBOTS = 'index, follow'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'pastie'
SITETITLE = 'Brian Mc Donald'
SITESUBTITLE = 'Humanitarian Information Management Specialist'
SITEDESCRIPTION = 'Sharing my thoughts on humanitarian data analysis'
PAGE_ORDER_BY = 'reversed-date'
STATIC_PATHS = ['files/pdfs', 'files/other', 'files/images', 'extra/favicon.ico', 'extra/favicon-16x16.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'extra/favicon-32x32.png'},
    'extra/apple-touch-icon.png': {'path': 'extra/apple-touch-icon.png'},
    'android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
}
ROBOTS = "index, follow"
