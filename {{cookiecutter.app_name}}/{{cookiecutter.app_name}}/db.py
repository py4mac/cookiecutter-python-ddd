import click

import {{cookiecutter.app_name}}.store.db.utils


@click.group("db")
def commands():
    """
    Commands for managing databases.
    """


@commands.command()
@click.argument("url", required=False)
def upgrade_db(url):
    """
    Upgrade database to the latest supported version.

    :param url of database
    """
    from {{cookiecutter.app_name}}.services.store._experiment_registry import utils

    url = url if url is not None else utils.get_experiment_uri()
    {{cookiecutter.app_name}}.store.db.utils.upgrade_sql_db(url)
