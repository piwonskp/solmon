from pathlib import Path

from anchorpy import Idl

API_URL = "https://api.devnet.solana.com"


def read_idl(idl):
    with Path(idl).open() as f:
        return Idl.from_json(f.read())
