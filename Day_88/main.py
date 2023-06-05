#!/usr/bin/env python

'''This module is used to create calculations functions such as addition, subtraction, multiplication and division
This module will also be invoked as a command line script.
'''

import click

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b


# Build a click group
@click.group()
def cli():
    '''This is a calculator app'''

@click.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add_command(a, b):
    click.echo(add(a, b))

@click.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def subtract_command(a, b):
    click.echo(subtraction(a, b))

# Add the commands to the CLI group
cli.add_command(add_command)
cli.add_command(subtract_command)

if __name__ == '__main__':
    cli()
