# -*- coding: utf-8 -*-

import subprocess


def test_commit_length(environment):
    template = environment.from_string('{% gitcommit %}')

    assert len(template.render()) == 40


def test_short_commit_length(environment):
    template = environment.from_string('{% gitcommit short=True %}')

    assert len(template.render()) == 7


def test_is_commit(environment):
    template = environment.from_string('{% gitcommit %}')
    output = subprocess.check_output(
        ['git', 'cat-file', '-t', template.render()],
    ).decode('utf-8').strip()

    assert output == 'commit'
