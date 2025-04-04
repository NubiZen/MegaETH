import os
from web3 import Web3
import json
from dotenv import load_dotenv
from eth_account import Account
from utils import web3, get_nonce, get_gas_price

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

CHAIN_ID = 6342

MINT_CONTRACT = Web3.to_checksum_address("0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f")

mint_abi = json.loads("""
[
  {
    "inputs": [
      {"internalType": "address","name": "to","type": "address"},
      {"internalType": "uint256","name": "amount","type": "uint256"}
    ],
    "name": "mint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
""")

contract = web3.eth.contract(address=MINT_CONTRACT, abi=mint_abi)

amount_to_mint = web3.to_wei(1000, "ether")

def mint_cusd():
    pk = Account._active_key
    account = Account.from_key(pk)
    wallet_address = account.address

    nonce = get_nonce(wallet_address)
    txn = contract.functions.mint(wallet_address, amount_to_mint).build_transaction({
        'from': wallet_address,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': get_gas_price(),
        'chainId': CHAIN_ID
    })
    signed_txn = web3.eth.account.sign_transaction(txn, pk)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"  Mint TX: {web3.to_hex(tx_hash)}")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        print("  cUSD minted!")
    else:
        raise Exception("Mint failed")