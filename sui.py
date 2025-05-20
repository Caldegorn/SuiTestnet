from pysdk_sui import Wallet

# Faucet and RPC URLs for Sui testnet
FAUCET_URL = 'https://faucet.testnet.sui.io/gas'
RPC_URL = 'https://fullnode.testnet.sui.io/'

# Your wallet mnemonic (keep this secret!)
MNEMONIC = 'your twelve word mnemonic phrase here'

# Initialize wallet instance
wallet = Wallet(rpc_url=RPC_URL, faucet_url=FAUCET_URL, mnemonic=MNEMONIC)

def auto_claim_faucet():
    # Request test tokens from the faucet
    response = wallet.request_tokens_from_faucet()
    print("Faucet response:", response)

    # Optional: check balance after faucet claim
    balance = wallet.get_balance()
    print(f"Current balance: {balance} MIST tokens")

if __name__ == '__main__':
    auto_claim_faucet()
