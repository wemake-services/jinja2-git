# -*- coding: utf-8 -*-

import subprocess

from jinja2 import nodes
from jinja2.ext import Extension


class GitExtension(Extension):
    """This class represents jinja2 extension to render current commit hash."""

    tags = {'gitcommit'}

    def _commit_hash(self):
        output = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        return output.decode('utf-8').strip()

    def parse(self, parser):
        """Main method to render data into the template."""
        lineno = next(parser.stream).lineno

        # TODO: add {% gitcommit 'short' %} feature
        result = self.call_method('_commit_hash', [], lineno=lineno)
        return nodes.Output([result], lineno=lineno)
