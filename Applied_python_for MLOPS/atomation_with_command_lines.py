# Click: A Python package for building command line interfaces.
import click

@click.command()
@click.option('--count', default=1)
def hello(count):
    for x in range(count):
        click.echo('Hello World!')

if __name__ == '__main__':
    hello()

  # ArgParse: A Python module for parsing command-line arguments.
  import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', action='store_true')
args = parser.parse_args()

if args.verbosity:
    print("Verbose mode enabled")

# sys.argv: A Python module containing command line arguments.
import sys 

print(f"Script name: {sys.argv[0]}")
print(f"First argument: {sys.argv[1]}") 
print(f"Second argument: {sys.argv[2]}")

# Setuptools: A package for building and distributing Python projects.
from setuptools import setup

setup(
    name='mypackage',
    version='1.0',
    install_requires=['requests', 'click']
)

# Entry points: Definitions linking scripts to functions in Setuptools.
from setuptools import setup

setup(
  #...,
  entry_points = {
    'console_scripts': [
      'myscript = mypackage.mymodule:main_func',
    ]  
  }
)
