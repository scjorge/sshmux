import click

from rich.console import Console
from rich.table import Table
from rich import box

#------------------------------------------------------------------------------
# COMMAND: group list
#------------------------------------------------------------------------------
@click.command(name="list", help="Lists all groups")
@click.pass_context
def cmd(ctx):
    config = ctx.obj['CONFIG']

    table = Table(box=box.SQUARE, style="grey39")
    table.add_column("Name", style="yellow")
    table.add_column("Hosts", justify="right", style="bright_yellow")
    table.add_column("Desc", style="gray50")

    for group in config:
        table.add_row(group["name"], str(len(group["hosts"])), group["desc"])

    console = Console()
    console.print(table)
