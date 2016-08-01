Design by contract in python- part three
########################################

:date: 2016-07-31 10:00
:tags: python
:category: blog
:slug: design-by-contract-in-python-part-three
:summary: Short description of libraries used to implement design by contract in python.
:header_cover: /images/covers/contract.jpg

**I covered py.contracts and zope.interface, now it's time to write about
abc module from python standard library.**

I wanted to write about another library `dpcontrancts <https://pypi.python.org/pypi/dpcontracts/0.1.0>`_,
but unfortunately, I wasn't able to download it from PyPi.

When I was reading and reviewing material for previous posts I found out that there is a way to
use python standard library ``abc.ABCMeta`` for contracts- I decided to give a try.

First, you have to know what are metaclasses: `understanding python metaclasses <https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/>`_
and what are they needed for: `Why use Abstract Base Classes in Python? <http://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python>`_.

After this introduction let's jump straight to the code:

.. code-block:: python

    import abc

    class ExternalAPIPortMetaclass(object, metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def search(self, query, *args, **kwargs):
            if not isinstance(query, str):
                raise ValueError('Query should be string')


    class ExternalAPIPort(ExternalAPIPortMetaclass):

        def __init__(self, adapter):
            self.adapter = adapter

        def search(self, query, *args, **kwargs):
            super(ExternalAPIPort, self).search(query, *args, **kwargs)
            return self.adapter.search(query, *args, **kwargs)

What is happening here? I defined ``ExternalAPIPortMetaclass`` as a metaclass that
inherits from ``abc.ABCMeta`` (This code snippet is valid for python 3). Then I
decided to make abstractmethod called ``search`` so all instances of that metaclass
will have to provide such function. Inside this code, I check whether provided
query is a string or not. In ``ExternalAPIPort`` which inherits from previously defined
I have to call super for ``ExternalAPIPortMetaclass`` search method. Thanks to
that I can make a validation of query. Right after that I simply return search query.

What I don't like there is fact that I need to add additional line of code inside
``ExternalAPIPort.search`` with ``super`` just for checking contract which can trick others.
That's why I think that metaclasses and contracts are two different topic besides that they
have some pieces in common (both are designed for telling: here I make contract that
you must obey).

To sum up this whole series I belive contracts are usefull for telling others that I made
agrement that this function has to take and return certain value. In python word where
is so called ducktyping and I don't think they are necessary in every case but designing by
contracts can be helpfull as I shown in examples. In my day to day work I use contracts
the same way to make agrements on ports methods in
`ports and adapters design pattern <{filename}/blog/ports_adapters1.rst>`_.

Thank you for reading! Feel free to comment!

Other blog posts in this series:
--------------------------------

- `Design by contract in python- part one <{filename}/blog/contracts1.rst>`_
- `Design by contract in python- part two <{filename}/blog/contracts2.rst>`_

Edits (01.08.2016):

* Add link to other posts with same series (thanks to `alb1 <https://www.reddit.com/user/alb1>`_)


Cover image under `CC0 <https://creativecommons.org/publicdomain/zero/1.0/deed.en>`_.
