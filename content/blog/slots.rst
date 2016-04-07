Python __slots__
################

:date: 2016-01-23 10:20
:tags: python
:category: blog
:slug: python-slots
:summary: Quick glance at python __slots__.
:header_cover: /images/covers/python.png

**Hello everyone in new layout of blog. Today I will write more about
python ``__slots__``.**

What exactly ``__slots__`` do? Imagine that you have a two python
classes- one with ``__slots__`` and other without:

.. code-block:: python

    class Slots(object):
        __slots__ = ['arg1', 'arg2']

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    class NoSlots(object):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

Then instantiate them:

.. code-block:: pycon

    >>> slots = Slots(arg1='first', arg2='second')
    >>> no_slots = NoSlots(arg1='third', arg3='fourth')


At first there is no much difference between ``slots`` and ``no_slots``
instances, but when we use ``dir()``:

.. code-block:: pycon

    >>> len(dir(slots))
    26
    >>> len(dir(no_slots))
    27

So what is different? The answer is slots got ``__slots__`` and
no\_slots: ``__dict__`` and ``__weakref__``. The implication of this is
as follows:

.. code-block:: pycon

    >>> slots.arg3 = 'fifth'
    AttributeError: 'Slots' object has no attribute 'arg3'
    >>> no_slots.arg3 = 'sixth'
    >>> no_slots.arg3
    'sixth'

Thanks to not having ``__dict__``. Slots class is a bit faster, but it's
impossible to add attribute that is not in ``__slots__``. Moreover there
is no ``__weakref__`` which means that it is not possible to cache this
object.

Cover image by `JohnsonMartin <https://pixabay.com/pl/users/JohnsonMartin-724525/>`_ under `CC0 <https://creativecommons.org/publicdomain/zero/1.0/>`_.
