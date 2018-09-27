# -*- coding: utf-8 -*-

import subprocess

from jinja2 import nodes
from jinja2.ext import Extension


class GitExtension(Extension):
    """This class represents jinja2 extension to render current commit hash."""

    tags = {'gitcommit'}

    def _commit_hash(self, short):
        params = ['git', 'rev-parse', 'HEAD']

        if short:
            params.insert(2, '--short')

        output = subprocess.check_output(params)
        return output.decode('utf-8').strip()

    def parse(self, parser):
        """Main method to render data into the template."""
        lineno = next(parser.stream).lineno

        if parser.stream.skip_if('name:short'):
            parser.stream.skip(1)
            short = parser.parse_expression()
        else:
            short = nodes.Const(False)

        result = self.call_method('_commit_hash', [short], [], lineno=lineno)
        return nodes.Output([result], lineno=lineno)
