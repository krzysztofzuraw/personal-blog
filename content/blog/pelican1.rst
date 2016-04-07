Moving blog to pelican
######################

:date: 2016-04-03 10:20
:tags: pelican, jekyll, nikola
:category: blog
:slug: moving-blog-to-pelican
:summary: Why I moved my blog to pelican.
:header_cover: /images/covers/pelican.jpg

**Hello! Spring has come so I decided that I need to changes- so I change my blog engine to** `pelican <http://blog.getpelican.com/>`_.

This blog will be about small compassion between three static site generators and why I choose pelican.

What are static site generators?

Basically they are engines that generates web sites using only static content. So there is no need for any backend or
database at all. Most of static site generators allow writing posts in markdown or rst formats.


Nikola
======

.. figure:: /images/nikola.png
   :alt: Nikola logo

When I started writing this blog I used a `Nikola <https://getnikola.com/>`_. What is it? It python powered static site generator.
I has a lot of features 'out of the box':

1. Incremental builds. That means only modified content is regenerated to html.
2. Support for comments. All you need to do is to set up option.
3. Support for IPython Notebooks.
4. Automatic deployment to Github pages.
5. Extensions to RST format.

I really enjoyed working with Nikola, but I changed it to another engine because I was overwhelmed by a lot of options
that I don't need. Also community is not huge but it is very helpful.

Jekyll
======

.. figure:: /images/jekyll.png
   :alt: Jekyll logo

Then I moved to `Jekyll <https://jekyllrb.com/>`_. This is ruby static site generator. What I like about jekyll is support for
`github pages <https://pages.github.com/>`_. Also is the most popular static site generator with a lot of community and themes. What I don't like is
it doesn't have support for tags out of the box. I know that it can be done by some ruby code, but I like this feature to be
build in. Moreover while you 'upload' your entire catalog with jekyll configuration your custom plugins don't work. You have
to stick to these provided in `github <https://pages.github.com/versions/>`_.

Pelican
=======

.. figure:: /images/pelican.png
    :alt: Pelican logo

So I decided to move to `pelican <http://blog.getpelican.com/>`_. What I like so far is that I have some more freedom to customize engine than in
nikola and I have out of the box support for tags. But there is thing: pelican only generates content. So you have to serve
it somehow. To do this I run simple python server. I don't like this approach- I want it to be automatic. I will write
next blog post about how to do this. Stay tuned!


Cover image by `Manjith Kainickara <https://www.flickr.com/photos/manjithkaini/>`_ under `CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0/>`_.
