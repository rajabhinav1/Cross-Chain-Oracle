import requests
import time

# Define the list of cryptocurrency symbols you want to fetch
crypto_symbols = ['bitcoin', 'ethereum', 'ripple', 'cardano', 'polkadot', 'litecoin', 'chainlink', 'stellar', 'binancecoin', 'bitcoin-cash',
                  'dogecoin', 'uniswap', 'vechain', 'tezos', 'eos']

# Define the currency
currency = 'usd'

def fetch_crypto_prices():
    crypto_prices = {}
    for crypto_symbol in crypto_symbols:
        api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={currency}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if crypto_symbol in data and currency in data[crypto_symbol]:
                price = data[crypto_symbol][currency]
                crypto_prices[crypto_symbol] = price
            else:
                print(f'Data not found for {crypto_symbol}.')
        else:
            print(f'Error fetching data for {crypto_symbol}.')
    return crypto_prices

while True:
    # Fetch and display cryptocurrency prices
    crypto_prices = fetch_crypto_prices()
    print('\nCryptocurrency Prices (in USD):')
    for crypto_symbol, price in crypto_prices.items():
        print(f'{crypto_symbol.upper()}: ${price:.2f}')

    # Ask the user to press Enter to refresh or 'q' to quit
    user_input = input('\nPress Enter to refresh or enter "q" to quit: ')
    if user_input.strip().lower() == 'q':
        break

