from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse
from web3 import Web3

app = Flask(__name__)
api = Api(app, version='1.0', title='Ethereum Contract API', description='API to interact with Ethereum smart contracts')

# Define the request parser
parser = reqparse.RequestParser()
parser.add_argument('abi', type=str, required=True, help='ABI of the Ethereum contract')
parser.add_argument('project_id', type=str, required=True, help='Infura Project ID')
parser.add_argument('contract_address', type=str, required=True, help='Contract address')

# Initialize a Web3 instance
web3 = None

@api.route('/contract_metadata')
class ContractMetadata(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()

        # Initialize Web3 instance if not already
        global web3
        if web3 is None:
            ethereum_url = f'https://mainnet.infura.io/v3/{args["project_id"]}'
            web3 = Web3(Web3.HTTPProvider(ethereum_url))

        # Decode ABI from hexadecimal
        abi_json = args['abi']

        try:
            # Create a contract object
            contract = web3.eth.contract(address=args['contract_address'], abi=abi_json)

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
            return {
                'error': str(e),
            }, 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
