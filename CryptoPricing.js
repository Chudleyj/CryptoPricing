var CoinMarketCap = require ("node-coinmarketcap");
var fs = require("fs");

var options = {
  events: true,
  refresh: 1,
  convert: "USD"
}

var arrayOfObjects;

fs.readFile('./Data.json', 'utf-8', function(err, data) {
	arrayOfObjects = JSON.parse(data)
})

var coinmarketcap = new CoinMarketCap(options);
var BTC;
var RIP;
var STEL;

coinmarketcap.on("BTC", (coin) => {
  BTC = coin.price_usd;
  arrayOfObjects.BitCoin.push({
		price: BTC
	})
});

coinmarketcap.on("ripple", (coin) => {
  RIP = coin.price_usd;
  arrayOfObjects.Ripple.push({
		price: RIP
	})
//  console.log(coin)
});

coinmarketcap.on("stellar", (coin) => {
  STEL = coin.price_usd;
  arrayOfObjects.Stellar.push({
		price: STEL
	})
//clears console  console.log('\033[2J');
  console.log("\n ................................................\n",
  "Stellar:", coin.price_usd, " BTC:", BTC, " Ripple:", RIP);
  fs.writeFile('./Data.json', JSON.stringify(arrayOfObjects), 'utf-8', function(err) {

  })
});

//STORING FORMAT FOR CLEARING JSON FILE HERE : {"BitCoin":[], "Ripple":[],"Stellar":[]}
