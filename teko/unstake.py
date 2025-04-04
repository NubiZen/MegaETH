import asyncio
from web3 import Web3
from teko.config import TEKO_STAKING_CONTRACT, TKUSDC_POOL_ID, CHAIN_ID
from teko.abi import TEKO_ABI
from utils import web3, get_nonce, get_gas_price
from eth_account import Account

async def unstake_tkusdc():
    pk = Account._active_key
    account = Account.from_key(pk)
    wallet_address = account.address

    contract = web3.eth.contract(address=TEKO_STAKING_CONTRACT, abi=TEKO_ABI)
    balance = contract.functions.getAssetsOf(TKUSDC_POOL_ID, wallet_address).call()
    print(f"  Available for unstake: {balance / 10**6} USDC")

    if balance == 0:
        print("  No tkUSDC available for unstake, skipping.")
        return

    print("  Sending unstake...")
    unstake_txn = contract.functions.withdraw(
        TKUSDC_POOL_ID, balance, wallet_address, wallet_address
    ).build_transaction({
        'from': wallet_address,
        'nonce': get_nonce(wallet_address),
        'gas': 300000,
        'gasPrice': get_gas_price(),
        'chainId': CHAIN_ID
    })
    
    signed_unstake = web3.eth.account.sign_transaction(unstake_txn, pk)
    unstake_hash = web3.eth.send_raw_transaction(signed_unstake.raw_transaction)
    print(f"  Unstake TX: {unstake_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(unstake_hash)
    if receipt['status'] == 1:
        print("  Successfully unstaked!")
    else:
        raise Exception("Unstaking failed")