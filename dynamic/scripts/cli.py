# Skeleton of a CLI

import click

import dynamic


@click.command('dynamic')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(dynamic.has_legs)
