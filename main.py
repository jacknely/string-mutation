#!/usr/bin/python3
"""A string mutation application."""
import click

from src.string_mutate import StringMutateService


@click.command()
@click.option('-w/-r')
@click.option(
    '--string', '-s', type=str, multiple=False, help='A string to mutate'
)
def string_mutation(string, w):
    """Mutate a string using the string mutate module."""
    service = StringMutateService()
    service.add_string(string)
    if w:
        reversed_string = service.reverse_words()
    else:
        reversed_string = service.reverse()

    click.echo(reversed_string)


if __name__ == '__main__':
    string_mutation()
