#!python
"""Command-line interface for hmp project."""

import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """My hmp project based upon Hypermodern Python project."""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="red")
    click.echo(textwrap.fill(page.extract))
