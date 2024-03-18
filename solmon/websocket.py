"""
WIP.
TODO: decode data returned by account subscribe and implement value comparison
"""

from asyncstdlib import enumerate
from solana.rpc.websocket_api import connect


async def monitor(
    idl, program_id, account_address, account_name, field, operator, reference_value
):
    async with connect("wss://api.devnet.solana.com") as websocket:
        await websocket.account_subscribe(account_address)
        first_resp = await websocket.recv()
        subscription_id = first_resp[0].result
        async for idx, msg in enumerate(websocket):
            if idx == 3:
                break
            print(msg)
        await websocket.logs_unsubscribe(subscription_id)
