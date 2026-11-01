import pytest
from jinja2 import Environment


@pytest.fixture
def environment() -> Environment:
    """Create jija2 environment for the tests."""
    return Environment(
        extensions=['jinja2_git.GitExtension'],
        autoescape=True,
    )
