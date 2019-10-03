# -*- coding: utf-8 -*-

import subprocess  # noqa: S404

from jinja2 import nodes
from jinja2.ext import Extension


class GitExtension(Extension):
    """This class represents jinja2 extension to render current commit hash."""

    tags = {'gitcommit'}

    def parse(self, parser):
        """Main method to render data into the template."""
        lineno = next(parser.stream).lineno

        if parser.stream.skip_if('name:short'):
            parser.stream.skip(1)
            short = parser.parse_expression()
        else:
            short = nodes.Const(False)  # noqa: WPS425

        commit = self.call_method('_commit_hash', [short], [], lineno=lineno)
        return nodes.Output([commit], lineno=lineno)

    def _commit_hash(self, short):
        command = ['git', 'rev-parse', 'HEAD']

        if short:
            command.insert(2, '--short')

        output = subprocess.check_output(command)  # noqa: S603
        return output.decode('utf-8').strip()
