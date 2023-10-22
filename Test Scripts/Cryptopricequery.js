const { app, BrowserWindow } = require('electron');
const request = require('request');
const path = require('path');
const url = require('url');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  mainWindow.loadURL(
    url.format({
      pathname: path.join(__dirname, 'index.html'),
      protocol: 'file:',
      slashes: true,
    })
  );

  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
  if (mainWindow === null) createWindow();
});

const cryptoSymbols = [
  'bitcoin', 'ethereum', 'ripple', 'cardano', 'polkadot', 'litecoin', 'chainlink', 'stellar', 'binancecoin', 'bitcoin-cash',
  'dogecoin', 'uniswap', 'vechain', 'tezos', 'eos'
];

const currency = 'usd';

const fetchCryptoPrices = () => {
  request(
    `https://api.coingecko.com/api/v3/simple/price?ids=${cryptoSymbols.join(',')}&vs_currencies=${currency}`,
    (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        const cryptoList = document.getElementById('crypto-list');
        cryptoList.innerHTML = '';
        Object.keys(data).forEach((symbol) => {
          const listItem = document.createElement('li');
          listItem.innerHTML = `${symbol.toUpperCase()}: $${data[symbol][currency].toFixed(2)}`;
          cryptoList.appendChild(listItem);
        });
      } else {
        console.error('Error fetching data:', error);
      }
    }
  );
};

const refreshButton = document.getElementById('refresh-button');
refreshButton.addEventListener('click', fetchCryptoPrices);
fetchCryptoPrices();
