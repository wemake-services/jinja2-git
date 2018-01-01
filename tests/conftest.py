# -*- coding: utf-8 -*-

import pytest
from jinja2 import Environment


@pytest.fixture(scope='function')
def environment():
    return Environment(extensions=['jinja2_git.GitExtension'])
