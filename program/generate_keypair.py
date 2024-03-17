from pathlib import Path

from solders.keypair import Keypair

keypair = Keypair()
filename = f"new-account-keypair-{keypair.pubkey()}.json"

print(f"Generated {filename}")

with Path(filename).open("w") as f:
    f.write(keypair.to_json())
