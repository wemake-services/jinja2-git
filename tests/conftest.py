import pytest
from jinja2 import Environment


@pytest.fixture()
def environment():
    return Environment(
        extensions=['jinja2_git.GitExtension'],
        autoescape=True,
    )
