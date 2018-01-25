var CoinMarketCap = require ("node-coinmarketcap");

var options = {
  events: true,
  refresh: 5,
  convert: "USD"
}

var coinmarketcap = new CoinMarketCap(options);
var BTC;
var RIP;
var STEL;

coinmarketcap.on("BTC", (coin) => {
  BTC = coin.price_usd;
});

coinmarketcap.on("ripple", (coin) => {
  RIP = coin.price_usd;
});

coinmarketcap.on("stellar", (coin) => {
  STEL = coin.price_usd;
//clears console  console.log('\033[2J');
  console.log("\n ................................................\n",
  "Stellar:", coin.price_usd, " BTC:", BTC, " Ripple:", RIP);
});
