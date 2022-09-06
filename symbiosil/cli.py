import multiprocessing
import os
import platform
import subprocess
from datetime import date, datetime, timezone
import click
from symetry.commons.preference import Preference
from symetry import environ

from symetry import settings

cli = click.Group()


@cli.command()
@click.option("--username", required=True, help="Enter username name.", prompt=True, )
def deleteuser(username, **kwargs):
    pass