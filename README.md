# Ethereum transaction signer
The program builds and signs Ethereum transaction and prints it in JSON format.

## Installation
> Program requires python3

Install python dependencies:

`$ pip3 install -r requirements.txt`

## Usage

Change example private key in code to your own:

```py
# Your eth private key
private_key = your_key
```

You can also customize web3 API endpoint by change the following line

```py
w3 = Web3(EthereumTesterProvider(PyEVMBackend()))
```

to something like this (depends on API that you use):

```py
# Infura
from web3 import HTTPProvider
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/..."))
```

Get signed transaction:

```
$ python3 sign-eth-tx.py --amount=<amount_in_ether> --to=<dest_address>
```

Example input:

```
$ python3 sign-eth-tx.py --amount=0.1 --to=0xB64fE1236f7D72c15Bffc6C529f750A8ACa4f8A2
```

Example output:
```json
{
    "raw": "0xf86b80830186a083088b8094b64fe1236f7d72c15bffc6c529f750a8aca4f8a288016345785d8a0000801ca0c2a4d2f471378c2f6b58cb7a3cb49b901fa9fd3c17115588609605fcb636d988a03fef678c875b3811042d204f062c2bdb91cb6b618be1467310032ee6f8fb1eaf",
    "tx": {
        "from": "0x9bf0de0Ae0B20824FF5bA31d40811b2195A99289",
        "to": "0xB64fE1236f7D72c15Bffc6C529f750A8ACa4f8A2",
        "gasPrice": 100000,
        "gas": 560000,
        "nonce": 0,
        "value": 100000000000000000,
        "v": 28,
        "r": 88039911500660287092820262787661862757072424883264378994978419880551612078472,
        "s": 28918700577748753850727394821041620247407314703228706280636314040420475281071,
        "hash": "0xdcd65ee1cd00a98445372fb260c248379eda57b354ee1e1e30b6323c97bdd7ed"
    }
}
```
