from web3 import Web3

# Reliable Sepolia RPC
RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def is_connected():
    return w3.is_connected()

def get_balance(address):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return float(balance_eth)