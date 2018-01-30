var CoinMarketCap = require ("node-coinmarketcap");
var Sequelize = require("sequelize");

var connection = new Sequelize('database', 'justin_chudley', 'password', {
  host: 'localhost',
  dialect: 'postgres',
  logging: false,
  operatorsAliases: false
});

var Cryptos = connection.define('cryptos', {
  Bitcoin: Sequelize.FLOAT,
  Ripple: Sequelize.FLOAT,
  Stellar: Sequelize.FLOAT
});

var options = {
  events: true,
  refresh: 1,
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
//  console.log(coin)
});

coinmarketcap.on("stellar", (coin) => {
  STEL = coin.price_usd;
//clears console  console.log('\033[2J');
  console.log("\n ................................................\n",
  "Stellar:", STEL, " BTC:", BTC, " Ripple:", RIP);
  updateDB();
});

function updateDB(){
  connection.sync().then(function (){
    Cryptos.create({
      Bitcoin: BTC,
      Ripple: RIP,
      Stellar: STEL
    });
  });
}
