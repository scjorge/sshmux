import click

from .config import config_del, config_set


# ------------------------------------------------------------------------------
# CONFIG Commands
# ------------------------------------------------------------------------------
@click.group(name="config", help="Modify SSHTMUX configuration trough SSH Config")
def ssh_config():
    pass


# // Linking other sub-commands
ssh_config.add_command(config_set.cmd)
ssh_config.add_command(config_del.cmd)
