import time
from operator import eq, ge, gt, le, lt, ne

from anchorpy import Program
from anchorpy.provider import Provider
from solana.rpc.async_api import AsyncClient

from solmon.lib import API_URL

OPERATIONS = {
    "lt": lt,
    "le": le,
    "gt": gt,
    "ge": ge,
    "eq": eq,
    "ne": ne,
}


async def fetch_account(idl, program_id, account_address, account_name):
    async with Program(
        idl, program_id, Provider(AsyncClient(API_URL), None)
    ) as program:
        return await program.account[account_name].fetch(account_address)


async def monitor(
    idl, program_id, account_address, account_name, field, operator, reference_value
):
    compare = OPERATIONS[operator]

    while True:
        state = await fetch_account(idl, program_id, account_address, account_name)
        current_value = getattr(state, field)
        cast = type(current_value)
        constraint_satisfied = compare(current_value, cast(reference_value))
        print("Validating constraint...")

        if not constraint_satisfied:
            print(
                f"WARNING: condition violated in {account_name}.{field}. Current value {current_value} expected to satisfy {operator} {reference_value}"
            )
        time.sleep(30)
