#!/usr/bin/python3
"""A string mutation application."""
from io import TextIOWrapper

import click

from src.string_mutate import StringMutateService


@click.command()
@click.option('-w/-r')
@click.argument('file', type=click.File('r'))
def string_mutation(file: TextIOWrapper, w: str) -> None:
    """Mutate a string using the string mutate module."""
    service = StringMutateService()
    data = file.read()
    service.add_string(data)
    if w:
        reversed_string = service.reverse_words()
    else:
        reversed_string = service.reverse()

    click.echo(reversed_string)


if __name__ == '__main__':
    string_mutation()
