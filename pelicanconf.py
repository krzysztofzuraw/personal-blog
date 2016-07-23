#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Krzysztof Żuraw'
SITENAME = u'Krzysztof Żuraw'
SITEURL = 'krzysztofzuraw.com'
SITESUBTITLE = 'Personal site'

TIMEZONE = 'Europe/Warsaw'
LOCALE = 'en_US.utf8'

THEME = 'pelican-clean-blog'
PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
SOCIAL = (('twitter', 'https://twitter.com/krzysztof_zuraw'),
          ('github', 'https://github.com/krzysztofzuraw'),
          ('envelope','mailto:krzysztof.zuraw@gmail.com'),
          ('linkedin', 'https://pl.linkedin.com/in/krzysztofzuraw'))

DEFAULT_PAGINATION = 5
MENUITEMS = (('Archive', '/archives.html'),
             ('Tags', '/tags.html'),
             ('Feeds', '/feeds/all.atom.xml'))

RELATIVE_URLS = False
DISQUS_SITENAME = 'krzysztofzuraw'
GOOGLE_ANALYTICS = 'UA-72188452-2'
HEADER_COVER = 'theme/images/codes.jpg'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
COLOR_SCHEME_CSS = 'monokai.css'
DIRECT_TEMPLATES = ['index', 'tags', 'archives']
STATIC_PATHS = ['images', 'videos', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
