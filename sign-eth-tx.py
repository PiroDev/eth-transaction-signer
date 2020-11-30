# Parse command-line args
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--amount", type=float, required=True, help="amount in ether")
parser.add_argument("--to", type=str, required=True, help="destination eth address")

args = parser.parse_args()

if args.amount < 0:
    print("Amount should be positive value!")
    exit(1)

print()

# Your eth private key
private_key = '0x92cf294b9a7a16d3147ee45736a6a4216d770d2e32aae52f0c2d96b5ea82d7ae'

from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
from eth_tester import PyEVMBackend

w3 = Web3(EthereumTesterProvider(PyEVMBackend()))

account = w3.eth.account.from_key(private_key)

tx = {
    "from": account.address,
    "to": args.to,
    "gasPrice": 100000, # Example gas price
    "gas": 560000, # Example gas amount
    "nonce": w3.eth.getTransactionCount(account.address),
    "value": w3.toWei(args.amount, "ether")
}

try:
    signed = account.signTransaction(tx)
except:
    print("Wrong address!")
    exit(2)

tx["v"] = signed.v
tx["r"] = signed.r
tx["s"] = signed.s
tx["hash"] = signed.hash.hex()


signed_transaction = {
    "raw": signed.rawTransaction.hex(),
    "tx": tx
}

import sys
import json
json.dump(signed_transaction, sys.stdout, indent=4, sort_keys=False)

print()
