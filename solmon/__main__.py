import asyncio

import click
from solders.pubkey import Pubkey

from solmon.http import OPERATIONS, monitor
from solmon.lib import read_idl


@click.command()
@click.argument("idl", type=read_idl)
@click.argument("program", type=Pubkey.from_string)
@click.argument("account_address", type=Pubkey.from_string)
@click.argument("account_name")
@click.argument("field")
@click.argument("operator", type=click.Choice(OPERATIONS.keys()))
@click.argument("value")
def main(idl, program, account_address, account_name, field, operator, value):
    asyncio.run(
        monitor(idl, program, account_address, account_name, field, operator, value)
    )


main()
