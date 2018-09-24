Jinja2 extension to handle git-specific things
==============================================

[![image](https://travis-ci.org/sobolevn/jinja2-git.svg?branch=master)](https://travis-ci.org/sobolevn/jinja2-git)
[![image](https://coveralls.io/repos/github/sobolevn/jinja2-git/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/jinja2-git?branch=master)
[![image](https://badge.fury.io/py/jinja2-git.svg)](http://badge.fury.io/py/jinja2-git)
[![image](https://img.shields.io/pypi/pyversions/jinja2-git.svg)](https://pypi.python.org/pypi/jinja2-git)

Reasoning
---------

This plugin is used to render commit hash in `jinja2` templates. We are
using it to render our template version in `cookicutter`:

-   [wemake-django-template](https://github.com/wemake-services/wemake-django-template)
-   [wemake-vue-template](https://github.com/wemake-services/wemake-vue-template)

Usage
-----

Add it as an extension for
[jinja2](http://jinja.pocoo.org/docs/2.10/extensions/) or
[cookiecutter](http://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html).

And then inside a template:

``` {.sourceCode .python}
from jinja2 import Environment

env = Environment(extensions=['jinja2_git.GitExtension'])
template = env.from_string('Commit is: {% gitcommit %}')
# => Commit is: c644682f4899d7e98147ce3a61a11bb13c52b3a0
```

Installation
------------

``` {.sourceCode .bash}
$ pip install jinja2-git
```
