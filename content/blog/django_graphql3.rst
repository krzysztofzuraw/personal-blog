Monorepo structure for Django & React Applications
##################################################

:date: 2017-08-20 10:00
:tags: django, python, javascript, react
:category: blog
:slug: monorepo-structure
:headline: Setting up React to work with Django
:header_cover: /images/covers/server.jpg

**Hello! Today I will guide you through setting up React application with Django! Let's get started!**

First thing is where I place my javascript application? Should it be in another repository? Or maybe Django should
use webpack to render js?

I decided to use pattern called ``monorepo``. What does it mean? It means that you will have your Django application in one
folder and React application in another folder under the **same** repository.

What are benefits of such approach? Deployment is a little bit easier as you deploy whole repository, not different services.
You can write integrations tests more easily. Everything will be governed by ``docker-compose``. Downsides? To release the only backend
you will have to release also frontend part.

So how will my folder structure look like?

.. code-block:: shell

    .
    ├── compose
    │   ├── django
    │   └── ui
    ├── film_api
    │   ├── config
    │   ├── film_database
    │   └── requirements
    └── film_ui
        ├── public
        └── src

So in ``film_api``, I keep all my backend service. In ``film_ui`` lays React code from `create-react-app <https://github.com/facebookincubator/create-react-app>`_.

How do I setup this everything? I use docker-compose:

.. code-block:: yml

    film_ui:
        build:
        context: .
        dockerfile: ./compose/ui/Dockerfile
        volumes:
        - ./film_ui/:/app
        - /app/node_modules
        command: yarn start
        ports:
        - "3000:3000"

The interesting setting here is volume ``/app/node_modules`` which allow docker to see node_modules from a host machine. I also use Dockerfile:

.. code-block:: dockerfile

    FROM node:8

    WORKDIR /app
    COPY ./film_ui/package.json /app
    COPY ./film_ui/yarn.lock /app

    RUN yarn install

    ADD ./film_ui/ /app

Thanks to such configuration I have live reloading and docker see changes that I made in the code base. This part was based on `Lessons from Building a Node App in Docker <http://jdlm.info/articles/2016/03/06/lessons-building-node-app-docker.html>`_.

That's all! I got my application ready to connect it to GraphQL so I will be displaying real data from the database instead of hard coded ones.

What's your approach to the structure of python with javascript application? Let me know in comments!

Other blog posts in this series:
--------------------------------

- `Django, GraphQL & React - part one <{filename}/blog/django_graphql1.rst>`_
- `Django, GraphQL & React - part two <{filename}/blog/django_graphql2.rst>`_
- `Moving to Relay in Django backend <{filename}/blog/django_graphql4.rst>`_

Repo with code can be found on `github <https://github.com/krzysztofzuraw/personal-blog-projects/tree/master/blog_django_graphql_react_relay>`_.



Cover image from `Unsplash <https://unsplash.com/search/server?photo=Re6__yidc48>`_ under
`CC0 <https://creativecommons.org/publicdomain/zero/1.0/>`_.
