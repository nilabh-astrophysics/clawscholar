import streamlit as st
from web3 import Web3

def get_balance():
    try:
        SEPOLIA_RPC = st.secrets.get("SEPOLIA_RPC")
        WALLET_ADDRESS = st.secrets.get("WALLET_ADDRESS")

        if not SEPOLIA_RPC or not WALLET_ADDRESS:
            return None

        w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC))

        if not w3.is_connected():
            return None

        checksum_address = Web3.to_checksum_address(WALLET_ADDRESS)
        balance_wei = w3.eth.get_balance(checksum_address)
        balance_eth = w3.from_wei(balance_wei, "ether")

        return float(balance_eth)

    except Exception:
        return None
