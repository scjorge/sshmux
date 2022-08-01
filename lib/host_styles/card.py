from lib.sshutils import SSH_Host

from rich.table import Table
from rich.panel import Panel
from rich import box

#------------------------------------------------------------------------------
# Render host data in panel with single-card look
#------------------------------------------------------------------------------
def render(host: SSH_Host):
    out_type = host.type if host.type == "normal" else f"[cyan]{host.type}[/]"
    out_info = "\n".join(host.info) if host.info else "- No info defined - "

    layout_table = Table("", box=box.ROUNDED, style="grey35" ,show_edge=True, show_header=False)
    layout_table.add_row(f"[bright_white]Name [/]:  {host.name}")
    layout_table.add_row(f"[bright_white]Group[/]:  {host.group}")
    layout_table.add_row(f"[bright_white]Type [/]:  {out_type}")

    if host.info:
        layout_table.add_row("")
        layout_table.add_row(f"[gray50]{out_info}[/]")

    layout_table.add_row("")

    param_table = Table(box=box.SIMPLE, style="grey35", show_header=True, show_edge=False, pad_edge=False)
    param_table.add_column("Param")
    param_table.add_column("Value")
    param_table.add_column("Inherited-from")

    # Add rows for SSH Config parameters
    for key, value in host.params.items():
        output_value = value if not isinstance(value, list) else "\n".join(value)
        param_table.add_row(key, output_value)

    # Add rows for inherited SSH Config parameters
    for pattern, pattern_params in host.inherited_params:
        for param, value in pattern_params.items():
            if not param in host.params:
                output_value = value if not isinstance(value, list) else "\n".join(value)
                param_table.add_row(param, output_value, pattern, style="yellow")

    layout_table.add_row(param_table)
    wrapper_panel = Panel(layout_table, box=box.SIMPLE, padding=(0,0))

    return wrapper_panel
