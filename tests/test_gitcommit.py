import subprocess

from jinja2 import Environment

_SHORT_COMMIT_LENGTH = 7
_FULL_COMMIT_LENGTH = 40


def test_commit_length(environment: Environment) -> None:
    template = environment.from_string('{% gitcommit %}')

    assert len(template.render()) == _FULL_COMMIT_LENGTH


def test_short_commit_length(environment: Environment) -> None:
    template = environment.from_string('{% gitcommit short=True %}')

    assert len(template.render()) == _SHORT_COMMIT_LENGTH


def test_is_commit(environment: Environment) -> None:
    template = environment.from_string('{% gitcommit %}')
    output = subprocess.check_output(
        ['git', 'cat-file', '-t', template.render()],
    ).decode('utf-8').strip()

    assert output == 'commit'
