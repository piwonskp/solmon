import asyncio
from pathlib import Path

import click
from anchorpy import Context, Program
from anchorpy.provider import Provider, Wallet
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import ID as SYS_PROGRAM_ID

from solmon.lib import API_URL, read_idl

PROGRAM_ID = "GXV2cYjG8ECRermN9f6X2zpsQsRqF34BEMNjGWGEqkCi"


def read_keypair(path):
    with Path(path).open() as f:
        return Keypair.from_json(f.read())


def get_accounts(wallet, account_address):
    return {
        "new_account": account_address,
        "signer": wallet.pubkey(),
        "system_program": SYS_PROGRAM_ID,
    }


def get_program(wallet, idl, program_id):
    return Program(idl, program_id, Provider(AsyncClient(API_URL), Wallet(wallet)))


@click.group()
@click.option("--wallet", type=read_keypair, required=True)
@click.option("--idl", type=read_idl, required=True)
@click.option("--program", type=Pubkey.from_string, default=PROGRAM_ID)
def cli(wallet, idl, program):
    pass


async def initalize(new_account, value, wallet, idl, program):
    async with get_program(wallet, idl, program) as program:
        await program.rpc["initialize"](
            value,
            ctx=Context(
                accounts=get_accounts(wallet, new_account.pubkey()),
                signers=[wallet, new_account],
            ),
        )


@cli.command("initialize")
@click.argument("account", type=read_keypair)
@click.argument("value", type=click.INT)
@click.pass_context
def initialize_cmd(ctx, account, value):
    asyncio.run(initalize(account, value, **ctx.parent.params))


async def modify_data(account_address, value, wallet, idl, program=PROGRAM_ID):
    async with get_program(wallet, idl, program) as program:
        await program.rpc["modify_data"](
            value,
            ctx=Context(
                accounts=get_accounts(wallet, account_address), signers=[wallet]
            ),
        )


@cli.command("modify_data")
@click.argument("account_address", type=Pubkey.from_string)
@click.argument("value", type=click.INT)
@click.pass_context
def modify_data_cmd(ctx, account_address, value):
    asyncio.run(modify_data(account_address, value, **ctx.parent.params))


cli()
