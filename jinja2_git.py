import subprocess  # noqa: S404

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.parser import Parser


class GitExtension(Extension):
    """This class represents jinja2 extension to render current commit hash."""

    tags = {'gitcommit'}

    def parse(self, parser: Parser) -> nodes.Output:
        """Main method to render data into the template."""
        lineno = next(parser.stream).lineno

        if parser.stream.skip_if('name:short'):
            parser.stream.skip(1)
            short = parser.parse_expression()
        else:
            short = nodes.Const(False)  # noqa: WPS425

        commit = self.call_method('_commit_hash', [short], [], lineno=lineno)
        return nodes.Output([commit], lineno=lineno)

    def _commit_hash(self, short: bool) -> str:
        command = [
            'git',
            'rev-parse',
            '--short' if short else '--verify',
            'HEAD',
        ]

        output = subprocess.check_output(command)  # noqa: S603
        return output.decode('utf-8').strip()
