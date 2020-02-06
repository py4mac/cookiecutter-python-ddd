import click

import {{cookiecutter.app_name}}.db
from {{cookiecutter.app_name}} import __version__


@click.group()
@click.version_option(__version__)
def cli():
    pass


cli.add_command({{cookiecutter.app_name}}.db.commands)

if __name__ == "__main__":
    cli()
