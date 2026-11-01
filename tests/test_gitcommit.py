import subprocess  # noqa: S404

from jinja2 import Environment

_SHORT_COMMIT_LENGTH = 7
_FULL_COMMIT_LENGTH = 40


def _assert_is_commit(template: str) -> None:
    commit = (
        subprocess  # noqa: S603
        .check_output(
            ['git', 'cat-file', '-t', template.render()],  # noqa: S607
        )
        .decode('utf-8')
        .strip()
    )

    assert commit == 'commit'


def test_commit_length(environment: Environment) -> None:
    """Test full commit."""
    template = environment.from_string('{% gitcommit %}')

    assert len(template.render()) == _FULL_COMMIT_LENGTH
    _assert_is_commit(template)


def test_short_commit_length(environment: Environment) -> None:
    """Test short commit."""
    template = environment.from_string('{% gitcommit short=True %}')

    assert len(template.render()) == _SHORT_COMMIT_LENGTH
    _assert_is_commit(template)
