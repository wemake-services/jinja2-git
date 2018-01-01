Jinja2 extension to handle git-specific things
----------------------------------------------

.. image:: https://travis-ci.org/sobolevn/jinja2-git.svg?branch=master
     :target: https://travis-ci.org/sobolevn/jinja2-git

.. image:: https://coveralls.io/repos/github/sobolevn/jinja2-git/badge.svg?branch=master
     :target: https://coveralls.io/github/sobolevn/jinja2-git?branch=master

.. image:: https://badge.fury.io/py/jinja2-git.svg
     :target: http://badge.fury.io/py/jinja2-git

.. image:: https://img.shields.io/pypi/pyversions/jinja2-git.svg
     :target: https://pypi.python.org/pypi/jinja2-git

Reasoning
~~~~~~~~~

This pligin is used to render commit hash in ``jinja2`` templates.
We are using it to render our template version in ``cookicutter``:

- `wemake-django-template <https://github.com/wemake-services/wemake-django-template>`_
- `wemake-vue-template <https://github.com/wemake-services/wemake-vue-template>`_

Usage
~~~~~

Add it as an extension for `jinja2 <http://jinja.pocoo.org/docs/2.10/extensions/>`_ or `cookiecutter <http://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html>`_.

And then inside a template:

.. code:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_git.GitExtension'])
    template = env.from_string('Commit is: {% gitcommit %}')
    # => Commit is: c644682f4899d7e98147ce3a61a11bb13c52b3a0


Installation
~~~~~~~~~~~~

.. code:: bash

    $ pip install jinja2-git
