async def send_gm():
    pk = Account._active_key
    account = Account.from_key(pk)
    wallet_address = account.address

    payload = "0x5011b71c"
    nonce = get_nonce(wallet_address)
    tx = {
        "from": wallet_address,
        "to": GM_CONTRACT,
        "data": payload,
        "value": web3.to_wei(0.0000001, "ether"),
        "gas": 300000,
        "gasPrice": get_gas_price(),
        "nonce": nonce,
        "chainId": CHAIN_ID,
    }
    signed_tx = web3.eth.account.sign_transaction(tx, pk)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_link = f"{tx_hash.hex()}"
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        return tx_link  # Mengembalikan link explorer
    else:
        raise Exception("GM sending failed")