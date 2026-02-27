# ============================
# CLAWSCHOLAR WALLET MODULE
# ============================

from web3 import Web3
import os

# Use environment variables (important for deployment)
SEPOLIA_RPC = os.getenv("SEPOLIA_RPC")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC))


def get_balance():
    """
    Returns wallet balance in ETH.
    Returns None if not connected.
    """

    if not w3.is_connected():
        return None

    try:
        balance_wei = w3.eth.get_balance(WALLET_ADDRESS)
        balance_eth = w3.from_wei(balance_wei, "ether")
        return float(balance_eth)

    except Exception as e:
        print("Wallet error:", e)
        return None