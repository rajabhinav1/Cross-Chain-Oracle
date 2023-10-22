import requests
import tkinter as tk

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

def display_crypto_prices():
    crypto_prices = fetch_crypto_prices()
    result_text.delete(1.0, tk.END)
    for crypto_symbol, price in crypto_prices.items():
        result_text.insert(tk.END, f'{crypto_symbol.upper()}: ${price:.2f}\n')

# Create a Tkinter window
root = tk.Tk()
root.title("Crypto Price Monitor")

# Create a refresh button
refresh_button = tk.Button(root, text="Refresh Prices", command=display_crypto_prices)
refresh_button.pack()

# Create a text widget to display prices
result_text = tk.Text(root, width=30, height=15)
result_text.pack()

# Initial display of crypto prices
display_crypto_prices()

# Run the Tkinter main loop
root.mainloop()
