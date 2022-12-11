import os
import json
from web3 import Web3
from web3 import web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account

from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract
    
st.title("Register New Artwork")
accounts = w3.eth.accounts
address = st.selectbox("Select Artwork Owner", options=accounts)
artwork_uri = st.text_input("The URI to the artwork")

if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({
        "from": address,
        "gas": 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
