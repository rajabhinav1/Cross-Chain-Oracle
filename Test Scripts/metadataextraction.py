import json
from web3 import Web3

# Replace with your Infura Project ID and Ethereum network URL
infura_project_id = 'c3399e1fc5cb4530870ff35cba7814e4'
ethereum_url = f'https://mainnet.infura.io/v3/{infura_project_id}'

# Initialize a Web3 instance
web3 = Web3(Web3.HTTPProvider(ethereum_url))

# ABI in hexadecimal format
abi_hex = "0x4a04594fef90fddf9bcc314772621877dd417875f61f2abd1370aff59b63b1bc"

# Remove the '0x' prefix and use the ABI as is
abi_json = abi_hex

# Contract address
contract_address = "0xDC951a24d37a24bb7F1423cFC825b81Dc92Be239"

def get_contract_metadata_and_timestamp(contract_address, abi_json):
    try:
        # Create a contract object
        contract = web3.eth.contract(address=contract_address, abi=abi_json)

        # Get contract metadata
        metadata = contract.functions.getSourceCode().call()

        # Get timestamp of the contract address creation
        creation_transaction = web3.eth.getTransaction(metadata['transactionHash'])
        timestamp = web3.toDatetime(creation_transaction['timestamp'], 's')

        return {
            'metadata': metadata,
            'timestamp': timestamp,
        }
    except Exception as e:
        print('Error fetching contract details:', str(e))
        raise e

# Example usage
contract_details = get_contract_metadata_and_timestamp(contract_address, abi_json)
print('Contract Metadata:', contract_details['metadata'])
print('Timestamp:', contract_details['timestamp'])
