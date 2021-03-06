#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Krzysztof Żuraw'
SITENAME = u'Krzysztof Żuraw'
SITEURL = ''
SITESUBTITLE = 'Personal site'

TIMEZONE = 'Europe/Warsaw'
LOCALE = 'en_US.utf8'

THEME = 'pelican-clean-blog'
PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

SOCIAL = (('twitter', 'https://twitter.com/krzysztof_zuraw'),
          ('github', 'https://github.com/krzysztofzuraw'),
          ('envelope', 'mailto:krzysztof.zuraw@gmail.com'),
          ('linkedin', 'https://pl.linkedin.com/in/krzysztofzuraw'))

DEFAULT_PAGINATION = 5
MENUITEMS = (('About', '/pages/about.html'),
             ('Archive', '/archives.html'),
             ('Tags', '/tags.html'),
             ('RSS Feed', 'http://feeds.feedburner.com/krzysztofzuraw'),
             ('Email Updates', 'https://feedburner.google.com/fb/a/mailverify?uri=krzysztofzuraw&amp;loc=en_US'))

RELATIVE_URLS = False
HEADER_COVER = 'theme/images/codes.jpg'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
COLOR_SCHEME_CSS = 'monokai.css'
DIRECT_TEMPLATES = ['index', 'tags', 'archives']
STATIC_PATHS = [
    'images', 'videos', 'extra/CNAME', 'extra/keybase.txt', 'extra/googlefda1a995d1b8808a.html',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/googlefda1a995d1b8808a.html': {'path': 'googlefda1a995d1b8808a.html'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
TWITTER_HANDLE = 'krzysztof_zuraw'
INDEX_TAGS = ['python', 'django', 'javscript']

PLUGINS = [
    'extended_sitemap'
]

EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'weekly',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}
