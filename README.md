# Jinja2 extension to handle git-specific things

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Travis](https://travis-ci.org/sobolevn/jinja2-git.svg?branch=master)](https://travis-ci.org/sobolevn/jinja2-git)
[![Coveralls](https://coveralls.io/repos/github/sobolevn/jinja2-git/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/jinja2-git?branch=master)
[![Python versions](https://img.shields.io/pypi/pyversions/jinja2-git.svg)](https://pypi.python.org/pypi/jinja2-git)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Installation

```bash
$ pip install jinja2-git
```


## Reasoning

This plugin is used to render commit hash in `jinja2` templates. We are
using it to render our template version in `cookicutter`:

- [wemake-django-template](https://github.com/wemake-services/wemake-django-template)
- [wemake-vue-template](https://github.com/wemake-services/wemake-vue-template)


## Usage

Add it as an extension for
[jinja2](http://jinja.pocoo.org/docs/2.10/extensions/) or
[cookiecutter](http://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html).

And then inside a template:

```python
from jinja2 import Environment

env = Environment(extensions=['jinja2_git.GitExtension'])
template = env.from_string('Commit is: {% gitcommit %}')
# => Commit is: c644682f4899d7e98147ce3a61a11bb13c52b3a0
```

Or short version:

```python
from jinja2 import Environment

env = Environment(extensions=['jinja2_git.GitExtension'])
template = env.from_string('Commit is: {% gitcommit short=True %}')
# => Commit is: c644682
```


## License

[MIT](https://github.com/sobolevn/jinja2-git/blob/master/LICENSE)
